import random
import time

def run_workload(cluster, duration_s, rps, get_ratio):
    start = time.time()
    ops = 0
    hits = 0

    while time.time() - start < duration_s:
        key = f"key{random.randint(1, 1000)}"
        if random.random() < get_ratio:
            val = cluster.get(key)
            if val is not None:
                hits += 1
        else:
            cluster.put(key, random.randint(1, 100000))
        ops += 1
        time.sleep(1 / rps)

    print("Ops:", ops)
    print("Hits:", hits)
    print("Hit rate:", hits / ops if ops else 0)
