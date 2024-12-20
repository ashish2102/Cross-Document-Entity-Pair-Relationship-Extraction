# utils/api_helper.py
import openai
from config import OPENAI_API_KEY, DEFAULT_MODEL, TEMPERATURE, MAX_TOKENS

openai.api_key = OPENAI_API_KEY

def call_openai_api(prompt, text):
    response = openai.ChatCompletion.create(
        model=DEFAULT_MODEL,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )
    return response.choices[0].message.content
