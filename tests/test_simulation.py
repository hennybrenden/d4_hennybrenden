# Henny Brenden

from walk.simulation import run_many

def test_run_many_outputs():
    stats = run_many(50, p_pentagon=1.0, p_kaia=0.0)
    assert stats["pct_pentagon"] == 1.0
