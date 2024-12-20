from neo4j import GraphDatabase
import json
import os
from rapidfuzz import fuzz
import uuid

# Define a class to build graph
class GraphBuilder:

    BIDIRECTIONAL_RELATIONSHIPS = {
        "Grandchild": "Grandparent",
        "Grandparent": "Grandchild",
        "Parent": "Child",
        "Child": "Parent",
        "Spouse": "Spouse",
        "Sibling": "Sibling",
        "Uncle": "Niece/Nephew",
        "Aunt": "Niece/Nephew",
        "Niece/Nephew": "Uncle/Aunt"
    }

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.name_to_uuid = {}  # In-memory mapping of names to UUIDs for fast access

    def close(self):
        self.driver.close()

    def add_person_with_uuid(self, name, metadata=None):
        "Add a person node with a UUID and attach metadata."
        # Generate a new UUID
        node_id = str(uuid.uuid4())  
        metadata = metadata or {}
        # Attach UUID to metadata
        metadata["node_id"] = node_id  
        with self.driver.session() as session:
            session.execute_write(self._add_person_with_uuid, node_id, name, metadata)

        # Update in-memory mapping
        self.name_to_uuid.setdefault(name, []).append(node_id)
        print(f"Added {name} with UUID {node_id}")
        # ###print(f"Current UUID Mapping: {self.name_to_uuid}")
        return node_id

    @staticmethod
    def _add_person_with_uuid(tx, node_id, name, metadata):
        tx.run("""
        MERGE (p:Person {node_id: $node_id})
        SET p.name = $name
        SET p += $metadata
        """, node_id=node_id, name=name, metadata=metadata)

    def get_nodes_with_name(self, name):
        "Retrieve all nodes with the same name, including their relationships and metadata."
        with self.driver.session() as session:
            nodes = session.execute_read(self._get_nodes_by_name, name)
        print(f"Retrieved nodes for name '{name}': {nodes}")
        return nodes

    @staticmethod
    def _get_nodes_by_name(tx, name):
        query = """
        MATCH (p:Person {name: $name})
        OPTIONAL MATCH (p)-[r]->(n)
        RETURN p.name AS name, p.node_id AS node_id, properties(p) AS metadata,
               collect({relationship: type(r), target: n.node_id}) AS relationships
        """
        result = tx.run(query, name=name)
        return [
            {
                "name": record["name"],
                "node_id": record["node_id"],
                "metadata": record["metadata"],
                "relationships": [
                    {"relationship": rel["relationship"], "target": rel["target"]}
                    for rel in record["relationships"] if rel["relationship"]
                ]
            }
            for record in result
        ]

    def infer_relationship(self, existing_node, relative_relationships):
        "Infer indirect relationships based on relatives of relatives."
        inferred_relationships = set()

        for rel in relative_relationships:
            if rel["relationship"] == "Spouse":
                inferred_relationships.add(("InLaw", rel["target"]))
            elif rel["relationship"] == "Parent":
                inferred_relationships.add(("Child", rel["target"]))
            elif rel["relationship"] == "Child":
                inferred_relationships.add(("Parent", rel["target"]))
            elif rel["relationship"] == "Sibling":
                inferred_relationships.add(("Sibling", rel["target"]))
            elif rel["relationship"] == "Grandparent":
                inferred_relationships.add(("Grandchild", rel["target"]))
            elif rel["relationship"] == "Grandchild":
                inferred_relationships.add(("Grandparent", rel["target"]))
            elif rel["relationship"] == "Uncle":
                inferred_relationships.add(("Niece/Nephew", rel["target"]))
            elif rel["relationship"] == "Aunt":
                inferred_relationships.add(("Niece/Nephew", rel["target"]))
            elif rel["relationship"] == "Niece/Nephew":
                inferred_relationships.add(("Uncle/Aunt", rel["target"]))
        return inferred_relationships

    def calculate_similarity(self, existing_node, new_metadata, new_relationships):
        "Calculate similarity score between an existing node and new data."
        score = 0

        # Metadata similarity
        existing_metadata = existing_node["metadata"]
        score += 0.4 if existing_metadata.get("birth_date") == new_metadata.get("BirthDate") else 0
        score += 0.3 if existing_metadata.get("birth_location") == new_metadata.get("BirthLocation") else 0
        score += 0.2 if existing_metadata.get("current_living_location") == new_metadata.get("CurrentLivingLocation") else 0

        # Name similarity
        score += (fuzz.ratio(existing_node["name"], new_metadata.get("Name", "")) / 100) * 0.1

        # Relationship similarity (with inference)
        existing_relationships = {f"{rel['relationship']}:{rel['target']}" for rel in existing_node["relationships"]}
        inferred_relationships = self.infer_relationship(existing_node, existing_node["relationships"])
        combined_relationships = existing_relationships.union(inferred_relationships)
        new_relationships_set = {f"{rel['relation']}:{rel['target']}" for rel in new_relationships}
        common = combined_relationships.intersection(new_relationships_set)
        score += len(common) * 0.1

        print(f"Similarity score for node '{existing_node['name']}': {score}")
        return score

    def relationship_exists(self, source_uuid, target_uuid, relationship):
        "Check if a relationship exists between two nodes."
        with self.driver.session() as session:
            exists = session.execute_read(self._relationship_exists, source_uuid, target_uuid, relationship)
        return exists

    @staticmethod
    def _relationship_exists(tx, source_uuid, target_uuid, relationship):
        query = """
        MATCH (a:Person {node_id: $source_uuid})-[r]->(b:Person {node_id: $target_uuid})
        WHERE type(r) = $relationship
        RETURN COUNT(r) AS count
        """
        result = tx.run(query, source_uuid=source_uuid, target_uuid=target_uuid, relationship=relationship)
        record = result.single()
        return record["count"] > 0 if record else False

    def add_relationship_with_names(self, source_name, target_name, relationship):
        "Add a relationship between two nodes by their names."
        source_uuid = self.get_uuid(source_name)
        target_uuid = self.get_uuid(target_name)

        # Validate UUIDs
        if not source_uuid:
            source_uuid = self.add_person_with_uuid(source_name)
        if not target_uuid:
            target_uuid = self.add_person_with_uuid(target_name)

        # Log the relationship attempt
        # ###print(f"Attempting to add relationship: {source_name} ({source_uuid}) -> {relationship} -> {target_name} ({target_uuid})")

        # Add the relationship
        self.add_relationship(source_uuid, target_uuid, relationship)

    def add_relationship(self, source_uuid, target_uuid, relationship):
        """
        Add a relationship between two nodes using their UUIDs.
        Automatically handle bidirectional relationships.
        """
        with self.driver.session() as session:
            try:
                # Add the original relationship
                session.execute_write(self._add_relationship, source_uuid, target_uuid, relationship)

                # Add the bidirectional relationship if applicable
                if relationship in self.BIDIRECTIONAL_RELATIONSHIPS:
                    reverse_relationship = self.BIDIRECTIONAL_RELATIONSHIPS[relationship]
                    session.execute_write(self._add_relationship, target_uuid, source_uuid, reverse_relationship)

                print(f"Added relationship: {source_uuid} -> {relationship} -> {target_uuid}")
                if relationship in self.BIDIRECTIONAL_RELATIONSHIPS:
                    print(f"Added reverse relationship: {target_uuid} -> {reverse_relationship} -> {source_uuid}")
            except Exception as e:
                print(f"Failed to add relationship: {e}")

    @staticmethod
    def _add_relationship(tx, source_uuid, target_uuid, relationship):
        "Safely create a relationship between two nodes using UUIDs and dynamic relationship type."
        if not source_uuid or not target_uuid:
            raise ValueError("Both source_uuid and target_uuid must be provided.")

        query = f"""
        MATCH (a:Person {{node_id: $source_uuid}}), (b:Person {{node_id: $target_uuid}})
        MERGE (a)-[r:{relationship}]->(b)
        RETURN r
        """
        # ###print(f"Executing query: {query} with source_uuid={source_uuid}, target_uuid={target_uuid}, relationship={relationship}")
        tx.run(query, source_uuid=source_uuid, target_uuid=target_uuid)

    def get_uuid(self, name):
        "Retrieve the UUID for a name from in-memory mapping or database."
        if name in self.name_to_uuid:
            return self.name_to_uuid[name][0]
        nodes = self.get_nodes_with_name(name)
        if nodes:
            return nodes[0]["node_id"]
        return None


def build_graph():
    print("Starting the graph-building process...")
    uri = "neo4j+s://128ce1cb.databases.neo4j.io"
    user = "neo4j"
    password = "Ipx4uQkGwzlkBA5Bm7LXgbJrTROCSk97aAJ2FkjapKk"
    graph = GraphBuilder(uri, user, password)

    outputs_path = "data/outputs"
    relation_file = os.path.join(outputs_path, "relation_output.json")
    metadata_file = os.path.join(outputs_path, "metadata_output.json")

    with open(relation_file, "r") as f:
        relation_data = json.load(f)
    with open(metadata_file, "r") as f:
        metadata_data = json.load(f)["metadata"]

    for rel in relation_data["relationships"]:
        source = rel["source"]
        target = rel["target"]
        relation = rel["relation"]

        print(f"Processing relationship: {source} -> {relation} -> {target}")
        #print(metadata_data, "\n"*5);
        source_metadata = next((m for m in metadata_data if m["Name"] == source), {})
        target_metadata = next((m for m in metadata_data if m["Name"] == target), {})

        source_nodes = graph.get_nodes_with_name(source)
        target_nodes = graph.get_nodes_with_name(target)

        # Log source node details
        if source_nodes:
            print(f"Source node '{source}' exists:")
            for node in source_nodes:
                similarity = graph.calculate_similarity(node, source_metadata, [rel])
                print(f"  - UUID: {node['node_id']}, Similarity Score: {similarity:.2f}")
        else:
            print(f"Source node '{source}' does not exist. Creating a new node...")
            graph.add_person_with_uuid(source, source_metadata)

        # Log target node details
        if target_nodes:
            print(f"Target node '{target}' exists:")
            for node in target_nodes:
                similarity = graph.calculate_similarity(node, target_metadata, [])
                print(f"  - UUID: {node['node_id']}, Similarity Score: {similarity:.2f}")
        else:
            print(f"Target node '{target}' does not exist. Creating a new node...")
            graph.add_person_with_uuid(target, target_metadata)

        graph.add_relationship_with_names(source, target, relation)

    print("\nGraph-building process completed successfully!")


if __name__ == "__main__":
    build_graph()
