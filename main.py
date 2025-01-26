import datetime
import math
import numpy as np
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="app.log",
    filemode="w",
)

class entitiy:
    def __init__(self):
        pass

    def decay(self):
        pass

    def evaluate(self):
        pass

class simulator:
    def __init__(self):
        self.entities = []

    

    def process(self):
        pass

    def decay(self):
        pass

    






    

    def add(self, entity):
        self.entities.append(entity)

        self.DECAY_RATE = 0
        self.DECAY_THRESHOLD = 0
        self.RANDOMNESS = 0
        self.ACTIVATION_PROB = 0
        self.SEED = 0
        self.SEED_MULTIPLIER = 0
        self.CYCLE_COUNT = 0
        self.CYCLE_TRIGGER = 0
        self.DECAY_WEIGHTS = {

        }
        self.BOOST = 0
        self.DECAY_REINFORCED = 0
        self.MAX_ENTITIES = 0
        self.PRUNE_THRESHOLD = 0
        self.SIMILARITY_THRESHOLD = 0





    def remove(self, entity):
        try:
            self.entities.remove(entity)
            print(f"Removed: {entity}")
        except ValueError:
            print(f"Entity not found: {entity}")
    
    def __len__(self):
            return len(self.entities)

    def __clear__(self):
        self.entities.clear()
        # self.entities = []