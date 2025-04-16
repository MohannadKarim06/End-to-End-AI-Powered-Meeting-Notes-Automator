import requests
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logs.logger import log_event

API_URL = "https://api.together.xyz/v1/chat/completions"
API_KEY = os.getenv("LLM_API_KEY")  

def llm_api(transcript: str):
    """
    Uses Together AI (Mistral) to extract action items from a meeting transcript.
    Returns a JSON-style string with task, assigned_to, and deadline.
    """

    instructions = (
        "You are an assistant that extracts structured action items from business meeting transcripts.\n"
        "Return ONLY a JSON list of action items, each with the following fields:\n"
        "- task: description of the task\n"
        "- assigned_to: the person responsible (if mentioned)\n"
        "- deadline: due date or deadline (if mentioned)\n"
        "Avoid any extra commentary or text outside the JSON structure."
    )

    prompt = f"""Transcript:
\"\"\"
{transcript}
\"\"\"
"""

    messages = [
        {"role": "system", "content": instructions},
        {"role": "user", "content": prompt}
    ]

    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "messages": messages,
        "temperature": 0.1,
        "top_p": 0.9,
        "max_tokens": 512,
        "repetition_penalty": 1.1
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code != 200:
            raise Exception(f"Together AI API Error: {response.status_code} {response.text}")

        result = response.json()
        return result["choices"][0]["message"]["content"].strip()

    except Exception as e:
        log_event("ERROR", f"Together AI error: {e}")
        return "Error: Unable to extract action items. Please try again later."


