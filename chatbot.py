import os
from dotenv import load_dotenv
import openai

load_dotenv()  # Load environment variables from .env

def get_chatbot_response(messages, model="gpt-4o-mini"):
    # Set API key and endpoint from environment variables
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_version = os.getenv("OPENAI_API_VERSION")
    if not api_key or not endpoint or not api_version:
        raise ValueError("AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, or OPENAI_API_VERSION not set in environment variables.")

    client = openai.AzureOpenAI(
        api_key=api_key,
        azure_endpoint=endpoint,
        api_version=api_version
    )
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content