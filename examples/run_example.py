# Henny Brenden

from walk.simulation import run_many

if __name__ == "__main__":
    stats = run_many(3000, p_pentagon=0.4, p_kaia=0.7)
    print(stats)


# This example runs the random walk simulation.
# With p_pentagon=0.4 and p_kaia=0.7, Alex most often ends up at Pentagon (~60%).