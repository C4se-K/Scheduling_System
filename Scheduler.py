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
    def __init__(self, id = -1, user = False, content = "", priority = -1, status = -1):
        self.ID = id
        self.USER = user
        self.CONTENT = content
        self.PRIORITY = priority
        self.STATUS = status
        self.AGE = time.time()

        self.RELEVANCE = self.evaluate()

    def info(self):
        return {
            "id": self.ID,
            "user": self.USER,
            "content": self.CONTENT,
            "priority": self.PRIORITY,
            "status": self.STATUS,
            "age": self.AGE,
            "relevance": self.RELEVANCE
        }
    
    def evaluate(self):
        weight_user = 0.3
        weight_priority = 0.4
        weight_status = 0.1
        weight_age = 0.2


        # 1 = 1x liklihood
        weight = 0

        #weight += 0
        #if time.time
        # todo
        """
        weights: dynamic...

        0   "id": None
        30  "user": True > False
        0   "content": None
        40  "priority": lower > higher
        10  "status": 3, 2, 1, 0 in order of priority
        20  "age": cur_time - age the larger the higher the priority
        -   "relevance": CUM SCORE
        
        """

        if self.USER:
            weight += 10 * weight_user

        if self.PRIORITY:
            weight += 10 * weight_priority

        if self.STATUS:
            temp = self.STATUS
            weight += (10 if temp == 3 else 
                       5 if temp == 2 else 
                       2 if temp == 1 else 
                       0) * weight_status
            
        if time.time() - self.AGE > 0:
            weight += 10 * weight_age

        #max score is 10, which means this item is 10 times more likely to be selected than an item with 1
        return int(weight) if weight > 0 else 1


class scheduler:
    def __init__(self):
        self.ENTITIES = []


        





        
    def process(self):
        pass


    def decay_all(self):
        pass

    
    def select(self):
        if not self.ENTITIES:
            logging.warning("no entities in scheduler")
            return
        
        id_list = [entity.ID for entity in self.ENTITIES]
        weight_list = [entity.RELEVANCE for entity in self.ENTITIES]

        item = random.choices(population = id_list, weights = weight_list, k = 1)
        if item:
            return item

    def add(self, id = -1, user = False, content = "", priority = -1, status = -1):
        self.ENTITIES.append(entity(id, user, content, priority, status))

    def remove(self, id):
        temp = None
        for entity in self.ENTITIES:
            if entity.ID == id:
                temp = entity
                break
        if temp:
            self.ENTITIES.remove(temp)

    def modify(self, id, user = None, content = None, priority = None, status = None, time = None):
        temp = None
        for entity in self.ENTITIES:
            if entity.ID == id:
                temp = entity
                break
        if temp:
            if user:
                pass
            if content:
                pass
            if priority:
                pass
            if status:
                pass
            if time:
                temp.AGE = time.time()



    def __len__(self):
            return len(self.ENTITIES)

    def __clear__(self):
        self.ENTITIES.clear()
        # self.ENTITIES = []



