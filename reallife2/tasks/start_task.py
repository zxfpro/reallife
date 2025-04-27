from reallife2.event.tips.start import ding_morning, change_frist

from reallife2.event.action.work import sync_ready_pool, sync_order_pool, sync_run_pool
from reallife2.event.action.notes import sync_note, sync_news
from reallife2.event.action.weight import sync_weight
from reallife2.event.action.cals import sync_calulate_func

def check_(func):
    result = func()
    if result:
        return result
    
def check_action_(func,debug=True):
    result = func()
    if result and debug:
        print('_____')


def start(debug=True):

    # 同步预备池   sync_ready_pool
    # 同步就绪池   sync_order_pool
    # 同步执行池   sync_run_pool
    # 同步体重    sync_weight
    # 同步日历    
    # 同步资讯    sync_news
    # 同步备忘录   sync_note
    # bulid知识库

    check_(ding_morning)

    
    result = sync_ready_pool()
    if result and debug:
        print('sync_ready_pool')

    result = sync_order_pool()
    if result and debug:
        print('sync_order_pool')
    
    check_(change_frist)



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


    result = sync_calulate_func()
    if result and debug:
        print('sync_calulate_func')

    result = sync_note()
    if result and debug:
        print('sync_note')
    
    return 'start over'
