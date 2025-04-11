from app.api.transciber_routes import transcriber_api
from utils import preprocess_transcription
import os, sys

from logs.logger import log_event

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def transcribe_audio(file):

    try:
        text = transcriber_api(file)
    except Exception as e:
        log_event("Error", f"Connection to trancribier API failed: {e}")

    try:
        chunks = preprocess_transcription(text)
    except Exception as e:
        log_event("Error", f"preprocessing transcription failed: {e}")
        

    return chunks
