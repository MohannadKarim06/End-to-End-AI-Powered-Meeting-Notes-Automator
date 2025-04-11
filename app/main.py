from fastapi import FastAPI
from pydantic import BaseModel
import os, sys

from logs.logger import log_event
from app.services.transcriber import transcribe_audio
from app.services.summarizer import summarize_text
from app.services.action_items_extractor import extract_action_items

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


app = FastAPI()

@app.post("/extract")
def extract(file):
    try:
        log_event("Stage 1", "Audio transribtion started!")
        text = transcribe_audio(file)
    except Exception as e:
        log_event("Error", f"Audio transcribion failed {e}")
        raise e

    try:
        log_event("Stage 2", "Transcription summarization started!")
        summary = summarize_text(text)

    except Exception as e:
        log_event("Error", f"Transcription summarization failed {e}")
        raise e

    try:
        log_event("Stage 3", "Action items extraction started!")
        action_items = extract_action_items(summary)
    except Exception as e:
        log_event("Error", f"Action items extraction failed {e}")
        raise e
        

    return {"summary": summary, "action_items": action_items}



