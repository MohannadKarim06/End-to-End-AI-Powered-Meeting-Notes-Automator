from utils import preprocess_transcripts
from app.api.transciber_routes import transcriber_api
import os, sys

from logs.logger import log_event

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def transcribe_audio(tmp_path):

    try:
        text = transcriber_api(tmp_path)
    except Exception as e:
        log_event("Error", f"Connection to trancribier API failed: {e}")

    try:
        text = preprocess_transcripts(text)
    except Exception as e:
        log_event("Error", f"preprocessing transcript failed: {e}")

    return text
