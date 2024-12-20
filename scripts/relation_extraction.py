# Import required libraries
import os
import sys
import openai
import json

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import OPENAI_API_KEY, DEFAULT_MODEL, TEMPERATURE, MAX_TOKENS
from ner_extraction import ner_extraction  # Import the NER function
from prompts.relation_prompt import relation_prompt  # Import the few-shot prompt

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

def relation_extraction(text):

    # Generate NER output
    ner_output = ner_extraction(text)
    if not ner_output:
        print("Failed to extract NER output.")
        return None
    
    # Prepare NER individuals for prompt context
    individuals = ner_output.get("individuals", [])
    ner_context = "\n".join([f"- {individual['name']}" for individual in individuals])

    # Combine the few-shot examples and NER output with the obituary text
    full_prompt = (relation_prompt + 
        "\n\nNER Output (Individuals Mentioned):\n" + ner_context + 
        "\n\nNow process the following obituary to extract relationships:\n" + text)
    system_message = (
        """You are a relationship extractor. Your task is to analyze the obituary and identify only direct relationships explicitly mentioned in the text. For each relationship, perform the following steps:

        Identify Direct Relationships: Extract only the direct relationships explicitly mentioned in the obituary. Avoid inferring or deducing indirect relationships.

        Convert the extracted relationships into the following standardized categories:

        Parent (e.g., 'father,' 'mother')
        Child (e.g., 'son,' 'daughter')
        Spouse (e.g., 'husband,' 'wife')
        Grandparent (e.g., 'grandfather,' 'grandmother')
        Grandchild (e.g., 'grandson,' 'granddaughter')

        Represent the extracted relationships in the JSON format.""")
    
    # API call
    response = openai.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": full_prompt}
        ],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )
    
    try:
        response_content = response.choices[0].message.content
        # Remove backticks if present
        if response_content.startswith("```json") and response_content.endswith("```"):
            response_content = response_content[7:-3].strip()
        return json.loads(response_content)
    
    except (KeyError, json.JSONDecodeError) as e:
        print("Error in response parsing:", e)
        print("Raw Response:", response)
        return None

# Example usage
if __name__ == "__main__":
    
    # Ensure the directory exists
    output_path = "C:/Users/dedee/Independent Study/Cross Document Knowledge Graph/data/outputs/relation_output.json"

    sample_obituary = "Joyce Lee Caudill went to be with the Lord on Saturday, October 5, 2024 at the age of 85.She was the daughter of the late Lee Worth and Mary Edith (Norman) Phipps born in Atkins, VA. and wife of the late Van Caudill.As a homemaker, Joyce enjoyed spending time with her family; sewing and playing scrabble.She is survived by her son, Paige Wayne Caudill of Elkton, Md; daughters, Gloria Faith Almony of Elkton, Md; Lorraine Hope Wilfong of Port Deposit, Md; Diane Charity McGonigal of Rising Sun, Md; and Pamela Joy Eckman of Peach Bottom, Pa. Siblings, Claudette Smith of Ruskin, FL; Melvin Phipps of Aberdeen, Md; several grandchildren and great grandchildren.In addition to her parents and husband, Joyce was preceded in death by her sons, Irvin Ward and Bradley Wade Caudill and siblings, Kelsey and William Phipps, Frances Jackson, Betty Lindsey and Mary Jane Hagan.A grave side service will be held on Thursday, October 10, 2024 at 10:00 AM at Harford Memorial Gardens in Havre de Grace, Md.In lieu of flowers, contributions can be made to Hospice Foundation of America."
    try:
        relations = relation_extraction(sample_obituary)
        if relations:
            with open(output_path, "w") as f:
                json.dump(relations, f, indent=4)
        print(relations)
    except Exception as e:
        print(f"An error occurred: {e}")
