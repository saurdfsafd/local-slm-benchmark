import json


def load_prompts(path="data/prompts.json"):
    with open(path, "r") as f:
        return json.load(f)


def save_results(results, path="reports/results.json"):
    with open(path, "w") as f:
        json.dump(results, f, indent=4)