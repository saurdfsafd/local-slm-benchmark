import time
import psutil


def capture_metrics(start_time):
    end_time = time.time()
    return {
        "latency": round(end_time - start_time, 3),
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent
    }