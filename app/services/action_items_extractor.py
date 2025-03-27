from app.api.action_items_routes import llm_api


def extract_action_items(text):

    try:
        text = llm_api(text)
    except Exception as e:
        log_event("Error", f"Connection to action items extractor API failed: {e}")


    return text