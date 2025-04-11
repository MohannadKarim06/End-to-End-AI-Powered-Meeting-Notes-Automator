import os, sys

from app.api.action_items_routes import llm_api
from logs.logger import log_event

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def extract_action_items(text):

    try:
        text = llm_api(text)
    except Exception as e:
        log_event("Error", f"Connection to action items extractor API failed: {e}")


    return text