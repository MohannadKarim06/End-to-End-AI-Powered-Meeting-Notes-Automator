import assemblyai as aai
import os

aai.settings.api_key = os.getenv("API_KEY_ASSEMBLY")

transcriber = aai.Transcriber()

def transcriber_api(tmp_path):

    transcript = transcriber.transcribe(tmp_path)

    return transcript.text
