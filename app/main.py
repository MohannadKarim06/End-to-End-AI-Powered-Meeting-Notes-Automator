from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import os, sys

from logs.logger import log_event
from app.services.transcriber import transcribe_audio
from app.services.summarizer import summarize_text
from app.services.action_items_extractor import extract_action_items

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


app = FastAPI()

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    temp_path = f"temp_audio/temp_{file.filename}"

    with open(temp_path, "wb") as f:
        f.write(await file.read())  

    try:
        log_event("Stage 1", "Audio transribtion started!")
        transcribtion = transcribe_audio(temp_path)
        return {"transcribtion": transcribtion}

    except Exception as e:
        log_event("Error", f"Audio transcribion failed {e}")

    finally:    
        if os.path.exists(temp_path):
            os.remove(temp_path)
            

@app.post("/summarize")
def summarize(text:str):
    
    try:
        log_event("Stage 2", "Transcription summarization started!")
        summary = summarize_text(text)

    except Exception as e:
        log_event("Error", f"Transcription summarization failed {e}")
        raise e

    
    return {"summary": summary}


@app.post("/action-items")
def extract_action_items(summary:str):
    
    try:
        log_event("Stage 3", "Action items extraction started!")
        action_items = extract_action_items(summary)
    except Exception as e:
        log_event("Error", f"Action items extraction failed {e}")
        raise e

    
    return {"action_items": action_items}








        
