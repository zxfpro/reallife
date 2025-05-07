""" 提供对外的方法 """

from datetime import datetime
from .logic import morning,evening,start_work,finish_work,tasks
from .event.utils import Date,push_task

date_c = Date()
DEBUG = False

def receive()->str:
    """领取一个任务(普通模式)

    Returns:
        str: 任务信息
    """
    time = date_c.time
    date = date_c.date
    time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S")
    # Create datetime objects once to avoid repetition
    time_8_50 = datetime.strptime(date + " 8:50:00", "%Y-%m-%d %H:%M:%S")
    time_10_00 = datetime.strptime(date + " 10:00:00", "%Y-%m-%d %H:%M:%S") 
    time_18_00 = datetime.strptime(date + " 18:00:00", "%Y-%m-%d %H:%M:%S")
    time_19_00 = datetime.strptime(date + " 19:00:00", "%Y-%m-%d %H:%M:%S")
    time_23_00 = datetime.strptime(date + " 23:00:00", "%Y-%m-%d %H:%M:%S")

    if time < time_8_50:
        if DEBUG:
            print('morning')
        return morning()

    if time_8_50 < time <= time_10_00:
        if DEBUG:
            print('start')
        return start_work(debug=DEBUG)

    if time_10_00 <= time < time_18_00:
        if DEBUG:
            print('tasks')
        return tasks()

    if time_18_00 <= time < time_19_00:
        if DEBUG:
            print('close')
        return finish_work()

    if time_19_00 <= time < time_23_00:
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
