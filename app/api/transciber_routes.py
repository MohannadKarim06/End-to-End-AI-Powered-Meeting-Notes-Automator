import os
from google.cloud import speech
from tempfile import NamedTemporaryFile

def transcriber_api(file):
    client = speech.SpeechClient()

    with NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(file.read())
        temp_audio.flush()

        with open(temp_audio.name, "rb") as audio_file:
            content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US"
    )

    response = client.recognize(config=config, audio=audio)

    full_text = " ".join([result.alternatives[0].transcript for result in response.results])
    return full_text
