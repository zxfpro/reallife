""" 逻辑覆盖能力 """
from .event.action import sync_calulate,sync_weight,sync_ready_pool,sync_order_pool
from .event.action import sync_run_pool, sync_note, sync_news, sync_note_night, recycle_tasks

from .event.tips import ding_morning,ding_evening
from .event.tips import change_frist,write_thinking,update_state_pause
from .event.tips import record_thinking,record_eatning,record_weight
from .event.tips import clean_cat_ning,clean_face,clean_ning,clean_room
from .event.tips import running,exercise,sleep,git_push_check
from .event.tips import check_chan,check_news

from .event.utils import run_shortcut
from .event.task_action import clean_and_update,edit_coder, test_and_study
from .event.task_action import design, meeting_and_talk, judge_type
from .event.task_action import task_failed,task_complete
from .event.utils import display_dialog,display_dialog_for_end

class TaskInfo(Exception):
    """任务的抛出机制

    Args:
        Exception (_type_): 抛出
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_(func):
    """检查信息的封装

    Args:
        func (object): 信息方法

    Raises:
        TaskInfo: 遇到信息抛出消息等待被捕捉
    """
    result = func()
    if result:
        raise TaskInfo(result)

def check_action_(func,debug=True):
    """一个执行动作的配装

    Args:
        func (object): 动作函数
        debug (bool, optional): 是否debug模式. Defaults to True.
    """
    result = func()
    if result and debug:
        print(func.__name__)

def morning()->str:
    """清晨动作

    Returns:
        str: 系统消息
    """
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

def start_work(debug=True)->str:
    """开工

    Args:
        debug (bool, optional): 是否调试模式. Defaults to True.

    Returns:
        str: 系统消息
    """
    try:
        check_(ding_morning)
        check_action_(sync_ready_pool,debug)
        check_action_(sync_order_pool,debug)
        check_action_(sync_weight,debug)

        check_(change_frist)
        check_action_(sync_run_pool,debug)
        # check_action_(sync_news) # 对方改版了,等着用pypeteer去做吧
        check_action_(sync_calulate,debug)
        check_action_(sync_note,debug)
        # bulid知识库
    except TaskInfo as e:
        return e

    return 'success'

def tasks():
    """任务列表

    Returns:
        str: 系统消息
    """
    try:
        check_(write_thinking)
        check_(update_state_pause)
        task = run_shortcut("获取任务")
        print("task:",task)
        if not task:
            return '无任务'
        task_type = judge_type(task)
        if task_type == "代码与练习":
            edit_coder(task)
        elif task_type == "实验与学习":
            test_and_study(task)
        elif task_type == "整理与优化":
            clean_and_update(task)
        elif task_type == "设计":
            design(task)
        elif task_type == "开会与对齐":
            meeting_and_talk(task)
        else:
            print('新的类别')
            # 开会与对齐
            meeting_and_talk(task)

        task_result = display_dialog_for_end("判断",f"任务是否完成: ",button_text="complete",button_text2="blockage",button_cancel=True)

        if task_result == 'complete':
            # 完成任务
            task_complete(task=task)
        
        elif task_result == 'blockage':
            # 任务阻塞
            #TODO
            pass

        else:
            # 完成未任务
            task_failed(task=task)

        
        # 移除完成的任务
        run_shortcut("移除完成的任务",task)

    except TaskInfo as e:
        return e

    return 'success'

def finish_work():
    """收工动作

    Returns:
        str: 系统信息
    """

    try:
        #TODO 知识库整理
        check_action_(recycle_tasks)
        check_action_(sync_note_night)
        check_(check_news)
        check_(check_chan)
        check_(git_push_check)
        check_(ding_evening)
    except TaskInfo as e:
        return e
    return 'success'

def evening()->str:
    """晚间休息的任务

    Returns:
        str: 系统消息
    """
    try:
        check_(clean_cat_ning)
        check_(clean_ning)
        check_(exercise)
        check_(sleep)
    except TaskInfo as e:
        return e

    return 'success'
