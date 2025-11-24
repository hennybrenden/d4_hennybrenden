# Henny Brenden

from .model import AlexWalk
import statistics

def run_many(n, *, p_pentagon=0.5, p_kaia=0.5, seed=42):
    rng = __import__("random").Random(seed)
    results = []

    for _ in range(n):
        walk = AlexWalk(p_pentagon=p_pentagon, p_kaia=p_kaia, rng=rng)
        results.append(walk.run())

    destinations = [r.destination for r in results]
    seconds = [r.seconds for r in results]
    steps = [r.steps for r in results]

    return {
        "n": n,
        "pct_kaia": destinations.count("kaia") / n,
        "pct_pentagon": destinations.count("pentagon") / n,
        "avg_seconds": statistics.mean(seconds),
        "avg_steps": statistics.mean(steps),
        "results": results,
    }

