import datetime
import time
from Scheduler import scheduler
import random


#testing
if __name__ == "__main__":
    scheduler_in = scheduler()

    short = []

    while True:
        scheduler_in.add(id = random.randint(1, 100))


        if len(short) < 5:
            short.append(scheduler_in.select())
        elif len(short) == 5:
            short.pop(0)
            


        

        print(short)
        time.sleep(0.25)



