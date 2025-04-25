from .status.utils import push_task,Date
date_c = Date()
date = date_c.date
from .status.info import *
from .status.action import *


from datetime import datetime

debug = True

def morning():
    result = record_thinking()
    if result:
        return result
    result = record_weight()
    if result:
        return result
    result = running()
    if result:
        return result
    result = record_eatning()
    if result:
        return result
    result = clean_face()
    if result:
        return result
    result = clean_room()
    if result:
        return result
    
def start():

    # 同步预备池   sync_ready_pool
    # 同步就绪池   sync_order_pool
    # 同步执行池   sync_run_pool
    # 同步体重    sync_weight
    # 同步日历    
    # 同步资讯    sync_news
    # 同步备忘录   sync_note
    # bulid知识库

    result = ding_morning()
    if result:
        if debug:
            print('ding_morning')
        return result
    
    result = sync_ready_pool()
    if result and debug:
        print('sync_ready_pool')

    result = sync_order_pool()
    if result and debug:
        print('sync_order_pool')
    
    result = change_frist()
    if result:
        if debug:
            print('change_frist')
        return result

    result = sync_run_pool()
    if result and debug:
        print('sync_run_pool')

    result = sync_weight()
    if result and debug:
        print('sync_weight')

    # 对方改版了,等着用pypeteer去做吧
    # result = sync_news()
    # if result and debug:
    #     print('sync_news')


    result = sync_calulate()
    if result and debug:
        print('sync_calulate')

    result = sync_note()
    if result and debug:
        print('sync_note')
    
    return 'start over'


def tasks():
    result = write_thinking()
    if result:
        if debug:
            print('write_thinking')
        return result
    

    
def close():
    # 知识库整理
    # 检查和收集咨询
    # 检查是否仍在禅模式
    # 执行池为完成的内容回归到就绪池
    # 同步酱油池
    result = git_push_check()
    if result:
        return result

    result = ding_evening()
    if result:
        return result
    
def evening():
    result = clean_cat_ning()
    if result:
        return result
    
    result = clean_ning()
    if result:
        return result
    
    result = exercise()
    if result:
        return result
    
    result = sleep()
    if result:
        return result


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