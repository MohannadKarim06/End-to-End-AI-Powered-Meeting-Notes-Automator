import requests


API_URL = os.getenv("API_URL")
API_TOKEN = os.getenv("API_TOKEN")

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def llm_api(text: str):
    prompt = f"""
You are an AI assistant that extracts action items from business meeting transcripts.

Your task is to identify all action items and return them in JSON format. Each action item should include:
- "task": a brief description of the task
- "assigned_to": the person responsible for the task (if mentioned)
- "deadline": the deadline for the task (if mentioned)

Transcript:
\"\"\"
{text}
\"\"\"
"""
    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": 0.5,
            "max_new_tokens": 512,
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Hugging Face API Error: {response.status_code} {response.text}")

    output = response.json()
    generated_text = output[0].get("generated_text", "").strip()

    

    return generated_text






