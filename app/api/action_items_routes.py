import requests
import os

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
API_TOKEN = os.getenv("HF_API_TOKEN")

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def llm_api(text: str):
    prompt = (
        "Extract the key action items from the meeting summary below. "
        "Respond ONLY with a JSON list where each action item has a 'task' and optionally an 'owner' and 'due_date'.\n\n"
        f"Meeting Summary:\n{text}\n\n"
        "Example Output:\n"
        "[{\"task\": \"Send client the updated roadmap\", \"owner\": \"Alex\", \"due_date\": \"next Monday\"},"
        "{\"task\": \"Schedule Q2 strategy meeting\"}]\n\n"
        "Now extract the action items:"
    )

    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Hugging Face API Error: {response.status_code} {response.text}")

    return response.json()[0]["generated_text"].strip()
