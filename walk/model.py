# Henny Brenden

import random

class SimulationResult:
    def __init__(self, destination, seconds, steps):
        self.destination = destination
        self.seconds = seconds
        self.steps = steps

class AlexWalk:
    def __init__(self, *,
                 x_pentagon=30,
                 x_audmax=50,
                 x_kaia=80,
                 p_pentagon=0.5,
                 p_kaia=0.5,
                 rng=None):
        self.pos = x_audmax
        self.x_pentagon = x_pentagon
        self.x_kaia = x_kaia
        self.p_pentagon = p_pentagon
        self.p_kaia = p_kaia
        self.rng = rng if rng is not None else random.Random()

        self.seconds = 0
        self.steps = 0

    def run(self):
        while True:
            self.seconds += 1

            if self.pos == self.x_pentagon:
                if self.rng.random() < self.p_pentagon:
                    return SimulationResult("pentagon", self.seconds, self.steps)

            if self.pos == self.x_kaia:
                if self.rng.random() < self.p_kaia:
                    return SimulationResult("kaia", self.seconds, self.steps)

            if self.rng.random() < 0.2:
                self.steps += 1
                if self.rng.random() < 0.5:
                    self.pos = max(0, self.pos - 1)
                else:
                    self.pos = min(100, self.pos + 1)

