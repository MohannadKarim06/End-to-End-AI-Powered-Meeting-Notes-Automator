import os, sys
import re
from app.api.action_items_routes import llm_api
from logs.logger import log_event

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def extract_action_items_json(text):
    
    action_items = []
    task_regex = r'"task":\s*"(.*?)"'
    assigned_to_regex = r'"assigned_to":\s*"(.*?)"'
    deadline_regex = r'"deadline":\s*"(.*?)"'

    tasks = re.findall(task_regex, text)
    assigned_tos = re.findall(assigned_to_regex, text)
    deadlines = re.findall(deadline_regex, text)

    num_action_items = len(tasks)  
    for i in range(num_action_items):
        action_item = {
            "task": tasks[i],
            "assigned_to": assigned_tos[i] if i < len(assigned_tos) else "N/A",
            "deadline": deadlines[i] if i < len(deadlines) else "N/A",
        }
        action_items.append(action_item)

    return action_items


def extract_action_items(text):

    try:
        text = llm_api(text)
        action_items = extract_action_items_json(text)
    except Exception as e:
        log_event("Error", f"Connection to action items extractor API failed: {e}")

    return action_items