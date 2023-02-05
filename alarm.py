import time 
import winsound 
from datetime import datetime,timedelta

alarm_time = datetime.now() + timedelta(seconds=30)

while True:
    if datetime.now() >= alarm_time:
        print("Time's Up!!")
        winsound.Beep(frequency=2500,duration=3000)
        break
    time.sleep(1)
