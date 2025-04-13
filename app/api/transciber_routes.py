import assemblyai as aai

aai.settings.api_key = "4a0c314ecc674175b7b8764986a7720f"

transcriber = aai.Transcriber()

def transcriber_api(tmp_path):

    transcript = transcriber.transcribe(tmp_path)

    return transcript.text
