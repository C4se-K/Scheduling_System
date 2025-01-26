import datetime
import time
from Scheduler import scheduler


#testing
if __name__ == "__main__":
    scheduler_in = scheduler()

    scheduler_in.add()

    while True:


        scheduler_in.add()

        print(scheduler_in.select(), scheduler_in.__len__())
        time.sleep(1)



