""" 提供对外的方法 """

from datetime import datetime
from .logic import morning,evening,start_work,finish_work,tasks
from .event.utils import Date,push_task

date_c = Date()
DEBUG = True

def receive()->str:
    """领取一个任务(普通模式)

    Returns:
        str: 任务信息
    """
    time = date_c.time
    date = date_c.date
    time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S")
    if time < datetime.strptime(date+" 8:50:00", "%Y-%m-%d %H:%M:%S"):
        if DEBUG:
            print('morning')
        return morning()

    if datetime.strptime(date+" 10:00:00", "%Y-%m-%d %H:%M:%S") > time >= \
       datetime.strptime(date+" 8:50:00", "%Y-%m-%d %H:%M:%S"):
        if DEBUG:
            print('start')
        return start_work()

    if datetime.strptime(date+" 18:00:00", "%Y-%m-%d %H:%M:%S") > time >= \
       datetime.strptime(date+" 10:00:00", "%Y-%m-%d %H:%M:%S"):
        if DEBUG:
            print('tasks')
        return tasks()

    if datetime.strptime(date+" 19:00:00", "%Y-%m-%d %H:%M:%S") > time >= \
       datetime.strptime(date+" 18:00:00", "%Y-%m-%d %H:%M:%S"):
        if DEBUG:
            print('close')
        return finish_work()

    if datetime.strptime(date+" 23:00:00", "%Y-%m-%d %H:%M:%S") > time >= \
       datetime.strptime(date+" 20:00:00", "%Y-%m-%d %H:%M:%S"):
        if DEBUG:
            print('evening')
        return evening()

    if DEBUG:
        print('end')
    return 'kong'

def complete():
    """完成当前任务
    """
    date = date_c.date
    task = receive()
    push_task(task=task,date=date)
