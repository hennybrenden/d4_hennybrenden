from walk.model import AlexWalk, SimulationResult

def test_walk_reaches_destination():
    walk = AlexWalk(
        x_pentagon=50, x_audmax=50,
        p_pentagon=1.0, p_kaia=0.0
    )
    result = walk.run()
    assert isinstance(result, SimulationResult)
    assert result.destination == "pentagon"

