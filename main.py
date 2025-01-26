import datetime
import math
import numpy as np
import logging
import threading
import time

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






class scheduler:
    def __init__(self):
        self.entities = []

        self.ACTIVE = False
        self.PROCESSING = False

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

    def decay(self):
        pass

    def run(self):
        while self.ACTIVE:
            try:
                if not self.PROCESSING:
                    pass








                time.sleep(1)
            except Exception as e:
                logging.exception(f"an exception occured in {self.__class__.__name__} : {e}")
            




    def start(self):
        if not self.ACTIVE:
            
            self.ACTIVE = True
            self.thread = threading.Thread(target=self.run, daemon=True)
            self.thread.start()

            logging.info("starting scheduler")
        else:
            logging.warning("scheduler is already running")


        

    def stop(self):
        if self.ACTIVE:
            
            self.ACTIVE = False
            if self.thread: 
                self.thread.join()

                logging.info("starting stopped")
        else:
            logging.warning("scheduler is not running")







    

    def add(self, entity):
        self.entities.append(entity)


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

if __name__ == "__main__":
    scheduler_in = scheduler()

    scheduler_in.start()

    scheduler_in.stop()