from app.api.transcriber_routes import transcriber_api
from utils import preprocess_transcription
from logs.logger import log_event


def transcribe_audio(file):

    try:
        text = transcriber_api(file)
    except Exception as e:
        log_event("Error", f"Connection to trancribier API failed: {e}")

    try:
        text = preprocess_transcription
    except Exception as e:
        log_event("Error", f"preprocessing transcription failed: {e}")
        

    return text
