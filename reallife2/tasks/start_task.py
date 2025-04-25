from .status.utils import push_task,Date
date_c = Date()
date = date_c.date
from .status.info import *
from .status.action import *


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
