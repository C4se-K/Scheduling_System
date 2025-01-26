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

class entity:
    def __init__(self, id = -1, task = False, content = "", priority = -1, status = -1):
        self.ID = id
        self.TASK = task
        self.CONTENT = content
        self.PRIORITY = priority
        self.STATUS = status
        self.AGE = time.time()

    def info(self):
        return {
            "id": self.ID,
            "task": self.TASK,
            "content": self.CONTENT,
            "priority": self.PRIORITY,
            "status": self.STATUS,
            "age": self.AGE,
        }


class scheduler:
    def __init__(self):
        self.ENTITIES = []


        





        
    def process(self):
        pass


    def decay_all(self):
        pass

    def evaluate(self, data):
        #print(data)
        return 1

    
    def select(self):
        if not self.ENTITIES:
            logging.warning("no entities in scheduler")
            return
        
        id_list = [entity.ID for entity in self.ENTITIES]
        weight_list = [self.evaluate(entity.info()) for entity in self.ENTITIES]

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
            





    def add(self, id = -1, task = False, content = "", priority = -1, status = -1):
        self.ENTITIES.append(entity(id, task, content, priority, status))

    def remove(self, id):
        temp = None
        for entity in self.ENTITIES:
            if entity.ID == id:
                temp = entity
                break
        if temp:
            self.ENTITIES.remove(temp)

    def __len__(self):
            return len(self.ENTITIES)

    def __clear__(self):
        self.ENTITIES.clear()
        # self.ENTITIES = []



