import datetime
import math
import numpy as np
import logging
import threading
import time
import random

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="app.log",
    filemode="w",
)

class entitiy:
    def __init__(self, id = -1, task = False, name = "", priority = -1, status = -1):
        self.ID = id
        self.TASK = task
        self.NAME = name
        self.PRIORITY = priority
        self.STATUS = status
        self.AGE = time.time

    def info(self):
        return {
            "id": self.ID,
            "task": self.TASK,
            "name": self.NAME,
            "priority": self.PRIORITY,
            "status": self.STATUS,
            "age": self.AGE,

        }






class scheduler:
    def __init__(self):
        self.ENTITIES = []


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





        
    def process(self):
        pass


    def decay_all(self):
        pass

    
    def select(self):
        if not self.ENTITIES:
            logging.warning("no entities in scheduler")
            return
        
        id_list = [entity['id'] for entity in self.ENTITIES]
        weight_list = [entity['weight'] for entity in self.ENTITIES]

        item = random.choices(id_list, weights = weight_list, k = 1)
        return item


    def get_entity(self):
        if not self.ENTITIES:
            logging.warning("no entities in scheduler")
            return

        self.process()
        self.select()
        self.decay_all()

        logging.info("returned entity")

        return
            





    def add(self, entity):
        self.ENTITIES.append(entity)

    def remove(self, entity):
        try:
            self.ENTITIES.remove(entity)
            print(f"Removed: {entity}")
        except ValueError:
            print(f"Entity not found: {entity}")
    
    def __len__(self):
            return len(self.ENTITIES)

    def __clear__(self):
        self.ENTITIES.clear()
        # self.ENTITIES = []



