Folder Structure
.
├── _pycache_               # Cached Python files
├── data
│   ├── outputs             # Processed outputs in JSON format
├── prompts
│   ├── metadata_prompt     # Prompt for metadata extraction
│   ├── ner_prompt          # Prompt for Named Entity Recognition
│   ├── relation_prompt     # Prompt for relationship extraction
├── scripts
│   ├── _pycache_           # Cached Python files
│   ├── ner_extraction.py   # Script for Named Entity Recognition
│   ├── relation_extraction.py # Script for relationship extraction
│   ├── metadata_extraction.py # Script for metadata extraction
│   ├── graph_builder.py    # Builds the knowledge graph from extracted data
│   ├── graph_updater.py    # Updates the graph with new data
├── utils
│   ├── api_helper.py       # Helper functions for API integration
├── config                  # Configuration files
├── main.py                 # Main execution script
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies


1. Prerequisites
Ensure you have the following installed:
Python 3.8+
Neo4j Community Edition (or Enterprise Edition)
Required Python libraries (install via requirements.txt)

2. Installation
Clone this repository:
git clone <repository-url>
cd Cross-Document-Knowledge-Graph

Install the required dependencies:
pip install -r requirements.txt

Set up a Neo4j instance:
Open Neo4j Cloud Aura and start the database server.
Create a new database and configure your credentials in the config directory.
Usage
1. Extract Data
Run the following scripts to process obituary text and extract information:
Named Entity Recognition:
python scripts/ner_extraction.py

Relationship Extraction:
python scripts/relation_extraction.py

Metadata Extraction:
python scripts/metadata_extraction.py
The outputs will be saved in the data/outputs directory as JSON files.

2. Build the Knowledge Graph
Once the data is extracted, construct the graph using:
python scripts/graph_builder.py

3. Update the Graph
To add new data or update existing relationships:
python scripts/graph_updater.py

4. Visualize the Knowledge Graph
Access the Neo4j browser and run Cypher queries to explore the graph:

Cypher query to visualize the Knowledge graph :
MATCH (a:Person)-[r]->(b:Person) RETURN a, r, b;

Key Scripts
ner_extraction.py: Extracts entities like names and places from obituary text.
relation_extraction.py: Identifies relationships such as Parent, Spouse, and Sibling.
metadata_extraction.py: Retrieves metadata (e.g., birth and death details) from the text.
graph_builder.py: Constructs the Neo4j knowledge graph from extracted data.
graph_updater.py: Updates the Neo4j graph with new or modified nodes and relationships.
api_helper.py: Provides helper functions for interacting with external APIs.


Technologies Used
Python: Core programming language.
Neo4j: Graph database for managing relationships.
OpenAI GPT: For extracting data with three shot prompting.
Cypher: Query language for Neo4j.
JSON: Data format for structured processing.


