import requests
import time
from app.metrics import capture_metrics
from app.config import OLLAMA_URL


def run_model(model, prompt):
    start = time.time()

    response = requests.post(OLLAMA_URL, json={
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_ctx": 512
        }
    })

    metrics = capture_metrics(start)

    try:
        output = response.json().get("response", "")
    except:
        output = "Error"

    return {
        "model": model,
        "prompt": prompt,
        "output": output,
        **metrics
    }