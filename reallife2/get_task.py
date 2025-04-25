from .status.utils import push_task,Date
date_c = Date()
date = date_c.date
from .status.info import *
from .status.action import *

from datetime import datetime

from reallife2.tasks.evening_task import evening,close
from reallife2.tasks.morning_task import morning
from reallife2.tasks.run_task import tasks
from reallife2.tasks.start_task import start

debug = True

def pull():
    # normal version
    time = date_c.time
    time = datetime.strptime(date_c.time, "%H:%M:%S")
    if debug:
        print('begin')
    if time < datetime.strptime("8:50:00", "%H:%M:%S"):
        if debug:
            print('morning')
        return morning()

    if datetime.strptime("10:00:00", "%H:%M:%S") > time >= datetime.strptime("8:50:00", "%H:%M:%S"):
        if debug:
            print('start')
        return start()

    if datetime.strptime("18:00:00", "%H:%M:%S") > time >= datetime.strptime("10:00:00", "%H:%M:%S"):
        if debug:
            print('tasks')
        return tasks()

    if datetime.strptime("19:00:00", "%H:%M:%S") > time >= datetime.strptime("18:00:00", "%H:%M:%S"):
        if debug:
            print('close')
        return close()

    
    if datetime.strptime("21:00:00", "%H:%M:%S") > time >= datetime.strptime("20:00:00", "%H:%M:%S"):
        if debug:
            print('evening')
        return evening()
    if debug:
        print('end')
def push():
    task = pull()
    push_task(task=task,date=date)
    return 'over'


if __name__ == "__main__":
    pull()