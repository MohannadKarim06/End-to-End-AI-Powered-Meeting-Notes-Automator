from app.api.summarizer_routes import summarization_api


def summarize_text(text):

    try:
       text = summarization_api(text)
    except Exception as e:
        log_event("Error", f"Connection to summarizer API failed: {e}")


   return text