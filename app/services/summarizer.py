import os, sys

from app.api.summarizer_routes import summarization_api
from logs.logger import log_event

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def summarize_text(text):

    try:
       text = summarization_api(text)
    except Exception as e:
        log_event("Error", f"Connection to summarizer API failed: {e}")


    return text