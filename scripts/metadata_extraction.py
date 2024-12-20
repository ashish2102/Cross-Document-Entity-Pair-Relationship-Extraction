# Import required libraries
import os
import sys
import openai
import json

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import OPENAI_API_KEY, TEMPERATURE, MAX_TOKENS, DEFAULT_MODEL
from prompts.metadata_prompt import metadata_prompt  # Import the few-shot prompt

# Set OpenAPI key
openai.api_key = OPENAI_API_KEY


# Define a function to extract named entities
def metadata_extraction(text):
    
    # Combine the few-shot examples with the new input
    full_prompt = metadata_prompt + f"\n\nNow process the following obituary and extract all the metadata in same JSON format:\n{text}"
    
    system_message = """You are a  biographical and relational metadata extractor specializing in identifying key details for all individuals mentioned in obituaries. Your task is to extract and provide metadata fields for each person referenced in the obituary, returning the information in JSON format. For each individual, extract the following fields when available:  
                        Name
                       Birth date
                       Birth location
                       Death date 
                       Death location 
                       Current living location
                       If a field is not mentioned, output it as null """
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
    # Extract and parse the assistant's response
    try:
        response_content = response.choices[0].message.content
        # Remove any backticks or code block markers if present
        if response_content.startswith("```json") and response_content.endswith("```"):
            response_content = response_content[7:-3].strip()

        # Parse the cleaned JSON string
        return json.loads(response_content)    
    except (KeyError, json.JSONDecodeError) as e:
        print("Error in response parsing:", e)
        print("Raw Response:", response)
        return None
    
# Get named entities for an obituary
if __name__ == "__main__":

    output_path = "data/outputs/metadata_output.json"

    sample_obituary = "Joyce Lee Caudill went to be with the Lord on Saturday, October 5, 2024 at the age of 85.She was the daughter of the late Lee Worth and Mary Edith (Norman) Phipps born in Atkins, VA. and wife of the late Van Caudill.As a homemaker, Joyce enjoyed spending time with her family; sewing and playing scrabble.She is survived by her son, Paige Wayne Caudill of Elkton, Md; daughters, Gloria Faith Almony of Elkton, Md; Lorraine Hope Wilfong of Port Deposit, Md; Diane Charity McGonigal of Rising Sun, Md; and Pamela Joy Eckman of Peach Bottom, Pa. Siblings, Claudette Smith of Ruskin, FL; Melvin Phipps of Aberdeen, Md; several grandchildren and great grandchildren.In addition to her parents and husband, Joyce was preceded in death by her sons, Irvin Ward and Bradley Wade Caudill and siblings, Kelsey and William Phipps, Frances Jackson, Betty Lindsey and Mary Jane Hagan.A grave side service will be held on Thursday, October 10, 2024 at 10:00 AM at Harford Memorial Gardens in Havre de Grace, Md.In lieu of flowers, contributions can be made to Hospice Foundation of America."
    print(sample_obituary)
    try:
        metadata_output = metadata_extraction(sample_obituary)
        if metadata_output:
            with open(output_path, "w") as f:
                json.dump(metadata_output, f, indent=4)
        print(metadata_output)
    except Exception as e:
        print(f"An error occurred: {e}")