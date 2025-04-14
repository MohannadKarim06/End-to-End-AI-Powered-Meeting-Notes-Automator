import requests
import os

API_URL = os.getenv("API_URL")
API_TOKEN = os.getenv("API_TOKEN")

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def summarization_api(text: str):
    payload = {
        "inputs": text,
        "parameters": {
            "do_sample": False,
            "max_length": 200,
            "min_length": 50
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Hugging Face Summarizer Error: {response.status_code} {response.text}")

    return response.json()[0]["summary_text"]

