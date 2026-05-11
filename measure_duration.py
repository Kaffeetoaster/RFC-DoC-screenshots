import time
import os

def measure(func,*args, **kwargs):
    start = time.perf_counter()
    print(f"Starting {func.__name__}... ")
    res = func(*args, **kwargs)
    end = time.perf_counter()
    duration = end - start
    print(f"Finished {func.__name__} in {duration:.6f}s ")

    with open("time.log", "a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} | {func.__name__} | {duration:.6f}s\n")

    return res


def start_new_log():
    with open("time.log", "a", encoding="utf-8") as f:
        f.write("="*50 + "\n")
        f.write(f"New log started at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

