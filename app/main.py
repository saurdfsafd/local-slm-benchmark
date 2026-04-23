from fastapi import FastAPI
from app.benchmark import run_benchmark
from app.utils import load_prompts, save_results

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Local SLM Benchmark API running"}


@app.get("/benchmark")
def benchmark():
    prompts = load_prompts()
    results = run_benchmark(prompts)
    save_results(results)
    return results