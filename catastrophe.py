import random


class Catastrophe:
    def __init__(self, probability):
        self.probability = probability

    def should_trigger(self):
        return random.random() < self.probability
