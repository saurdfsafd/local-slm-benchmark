from app.model_runner import run_model
from app.config import MODELS


def run_benchmark(prompts):
    results = []

    for prompt in prompts:
        for model in MODELS:
            print(f"Running {model}...")
            result = run_model(model, prompt)
            results.append(result)

    return results