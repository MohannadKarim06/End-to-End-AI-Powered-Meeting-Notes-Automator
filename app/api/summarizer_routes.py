import requests
import os

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
API_TOKEN = "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"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def summarization_api(text: str):
    payload = {
        "inputs": text,
        "parameters": {
            "min_length": 30,
            "max_length": 200,
            "do_sample": False
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Hugging Face Summarizer Error: {response.status_code} {response.text}")

    return response.json()[0]["summary_text"]

