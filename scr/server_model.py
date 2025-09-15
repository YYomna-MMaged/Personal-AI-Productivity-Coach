import requests
from scr.retriever import get_collection, retrieve
from scr.llm_prompts import daily_analysis_prompt, task_organization_prompt

API_KEY = ""
NGROK_URL = "" 

def call_remote_model(prompt: str, max_length: int = 500):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {"prompt": prompt}

    response = requests.post(f"{NGROK_URL}/generate", headers=headers, json=data)
    response.raise_for_status()
    return response.json()["response"]


def analyze_day_report(user_text):
    kb_context = retrieve(query = user_text)
    prompt = daily_analysis_prompt(user_text, kb_context = kb_context)
    return call_remote_model(prompt)


def analyze_tasks(tasks_text):
    prompt = task_organization_prompt(tasks_text)
    return call_remote_model(prompt)
