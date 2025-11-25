# Henny Brenden

import random

class SimulationResult:
    def __init__(self, ended_at, seconds, steps):
        self.ended_at = ended_at      # "kaia" eller "pentagon"
        self.seconds = seconds        # total tid
        self.steps = steps            # antall steg


class AlexWalk:
    def __init__(
        self,
        p_pentagon=0.5,
        p_kaia=0.5,
        start=50,         # AudMax
        pentagon=30,
        kaia=80,
    ):
        self.pos = start
        self.p_pentagon = p_pentagon
        self.p_kaia = p_kaia
        self.pentagon = pentagon
        self.kaia = kaia

        self.seconds = 0
        self.steps = 0

    def step(self):
        """Alex takes a random step with 20% probability."""
        # 20% chance to move
        if random.random() < 0.2:
            # 50/50 east or west
            if random.random() < 0.5:
                self.pos += 1
            else:
                self.pos -= 1

            # Keep within 0–100
            self.pos = max(0, min(100, self.pos))
            self.steps += 1

    def run(self):
        """Run the walk until Alex is absorbed."""
        while True:
            # Increase time
            self.seconds += 1

            # Pentagon check
            if self.pos == self.pentagon:
                if random.random() < self.p_pentagon:
                    return SimulationResult("pentagon", self.seconds, self.steps)

            # Kaia check
            if self.pos == self.kaia:
                if random.random() < self.p_kaia:
                    return SimulationResult("kaia", self.seconds, self.steps)

            # If not absorbed: move
            self.step()
