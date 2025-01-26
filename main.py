import datetime
import time
from Scheduler import scheduler


#testing
if __name__ == "__main__":
    scheduler_in = scheduler()

    while True:

        scheduler_in.run()

        scheduler_in.stop()
        time.sleep (2)