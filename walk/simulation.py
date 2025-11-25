# Henny Brenden

from .model import AlexWalk

def run_many(n, p_pentagon, p_kaia):
    results = []

    for _ in range(n):
        walk = AlexWalk(
            p_pentagon=p_pentagon,
            p_kaia=p_kaia,
        )
        res = walk.run()
        results.append(res)

    total = len(results)
    n_kaia = sum(r.ended_at == "kaia" for r in results)
    n_pentagon = sum(r.ended_at == "pentagon" for r in results)

    pct_kaia = n_kaia / total
    pct_pentagon = n_pentagon / total
    avg_seconds = sum(r.seconds for r in results) / total
    avg_steps = sum(r.steps for r in results) / total

    return {
        "pct_kaia": pct_kaia,
        "pct_pentagon": pct_pentagon,
        "avg_seconds": avg_seconds,
        "avg_steps": avg_steps,
    }
