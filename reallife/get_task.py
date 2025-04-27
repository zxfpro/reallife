from .utils.manager_utils import Date,push_task
date_c = Date()
date = date_c.date

from datetime import datetime

from .tasks import morning,evening,start_work,finish_work,tasks

debug = True

def pull():
    # normal version
    time = date_c.time
    date = date_c.date
    time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S")
    if time < datetime.strptime(date+" 8:50:00", "%Y-%m-%d %H:%M:%S"):
        if debug:
            print('morning')
        return morning()

    if datetime.strptime(date+" 10:00:00", "%Y-%m-%d %H:%M:%S") > time >= datetime.strptime(date+" 8:50:00", "%Y-%m-%d %H:%M:%S"):
        if debug:
            print('start')
        return start_work()

    if datetime.strptime(date+" 18:00:00", "%Y-%m-%d %H:%M:%S") > time >= datetime.strptime(date+" 10:00:00", "%Y-%m-%d %H:%M:%S"):
        if debug:
            print('tasks')
        return tasks()

    if datetime.strptime(date+" 19:00:00", "%Y-%m-%d %H:%M:%S") > time >= datetime.strptime(date+" 18:00:00", "%Y-%m-%d %H:%M:%S"):
        if debug:
            print('close')
        return finish_work()

    
    if datetime.strptime(date+" 21:00:00", "%Y-%m-%d %H:%M:%S") > time >= datetime.strptime(date+" 20:00:00", "%Y-%m-%d %H:%M:%S"):
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