from .event.action import sync_calulate,sync_weight,sync_ready_pool,sync_order_pool
from .event.action import sync_run_pool, sync_note, sync_news

from .event.tips import ding_morning,ding_evening
from .event.tips import change_frist,write_thinking
from .event.tips import record_thinking,record_eatning,record_weight
from .event.tips import clean_cat_ning,clean_face,clean_ning,clean_room
from .event.tips import running,exercise,sleep,git_push_check

from .utils.utils import run_shortcut
from .event.run_tasks import clean_and_update,edit_coder, test_and_study, clean_and_update
from .event.run_tasks import design, meeting_and_talk, judge_type
# source ~/.bash_profile ;cd /Users/zhaoxuefeng/GitHub/aiworker; .venv/bin/python script/kanban_manager_add_tips.py

class TaskInfo(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def run_task():
    # 跟进阻塞池

    #get_task 得到一个任务
    task = run_shortcut("获取任务")
    print(task,'task')

    # 判断这个任务属于哪种类型

    task_type = judge_type(task)

    if task_type == "编写代码":
        edit_coder()

    elif task_type == "实验与学习":
        test_and_study()

    elif task_type == "整理与优化":
        clean_and_update()

    elif task_type == "设计":
        design(task)

    elif task_type == "开会与对齐":
        meeting_and_talk(task)

    else:
        print('新的类别')
        # 开会与对齐
        meeting_and_talk(task)

    # 是否完成任务

        # 完成任务

        # 非完成任务
    


    # 移除完成的任务
    task = run_shortcut("移除完成的任务")



def check_(func):
    result = func()
    if result:
        raise TaskInfo(result)

def check_action_(func,debug=True):
    result = func()
    if result and debug:
        print(func.__name__)
    
def morning():
    try:
        check_(record_thinking)
        check_(record_weight)
        check_(running)
        check_(record_eatning)
        check_(clean_face)
        check_(clean_room)
    except TaskInfo as e:
        return e

    return 'success'


def start_work(debug=True):

    # 同步预备池   sync_ready_pool
    # 同步就绪池   sync_order_pool
    # 同步执行池   sync_run_pool
    # 同步体重    sync_weight
    # 同步日历    
    # 同步资讯    sync_news
    # 同步备忘录   sync_note
    # bulid知识库
    try:
        check_(ding_morning)
        check_action_(sync_ready_pool,debug)
        check_action_(sync_order_pool,debug)
        check_action_(sync_weight,debug)

        check_(change_frist)
        check_action_(sync_run_pool,debug)
        # check_action_(sync_news) # 对方改版了,等着用pypeteer去做吧
        check_action_(sync_calulate)
        check_action_(sync_note)
    except TaskInfo as e:
        return e

    return 'success'

def tasks():
    try:
        check_(write_thinking)
        run_task()
    except TaskInfo as e:
            return e

    return 'success'


def finish_work():
    # 知识库整理
    # 检查和收集咨询
    # 检查是否仍在禅模式
    # 执行池为完成的内容回归到就绪池
    # 同步酱油池

    try:
        check_(git_push_check)
        check_(ding_evening)
    except TaskInfo as e:
            return e

    return 'success'

    

def evening():
    try:
        check_(clean_cat_ning)
        check_(clean_ning)
        check_(exercise)
        check_(sleep)
    except TaskInfo as e:
            return e

    return 'success'

