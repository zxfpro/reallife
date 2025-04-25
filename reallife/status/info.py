"""提供一些带状态的消息"""

from .utils import status, Date
date_c = Date()
date = date_c.date

# morning
@status(task='记录灵感',date=date)
def record_thinking():
    """提醒

    Returns:
        str: 任务内容
    """
    return "记录灵感"

@status(task='记录体重',date=date)
def record_weight():
    """提醒

    Returns:
        str: 任务内容
    """
    # 记录体重比较特殊
    return "记录体重"

@status(task='跑步',date=date)
def running():
    """提醒

    Returns:
        str: 任务内容
    """
    return "跑步"

@status(task='记录吃了什么',date=date)
def record_eatning():
    """提醒

    Returns:
        str: 任务内容
    """
    return "记录吃了什么"

@status(task='洗漱护肤',date=date)
def clean_face():
    """提醒

    Returns:
        str: 任务内容
    """
    return "洗漱护肤"

@status(task='收拾家与锻炼',date=date)
def clean_room():
    """提醒

    Returns:
        str: 任务内容
    """
    return "收拾家与锻炼"

# start

@status(task='上班打卡',date=date)
def ding_morning():
    """提醒

    Returns:
        str: 任务内容
    """
    return "上班打卡"


@status(task='调整优先级',date=date)
def change_frist():
    """提醒

    Returns:
        str: 任务内容
    """
    return "调整优先级"

@status(task='上传到日历',date=date)
def update_to_cal():
    """提醒

    Returns:
        str: 任务内容
    """
    return "上传到日历"

# tasks
@status(task='写下灵感',date=date)
def write_thinking():
    """提醒

    Returns:
        str: 任务内容
    """
    return "写下灵感"



# close

@status(task='下班打卡',date=date)
def ding_evening():
    """提醒

    Returns:
        str: 任务内容
    """
    return "下班打卡"


@status(task='检测git提交',date=date)
def git_push_check():
    """提醒

    Returns:
        str: 任务内容
    """
    return "检测git提交"


# evening
@status(task='整理家里和猫猫',date=date)
def clean_cat_ning():
    """提醒

    Returns:
        str: 任务内容
    """
    return "整理家里和猫猫"

@status(task='晚上洗漱,刷牙,护肤',date=date)
def clean_ning():
    """提醒

    Returns:
        str: 任务内容
    """
    return "晚上洗漱,刷牙,护肤"

@status(task='锻炼',date=date)
def exercise():
    """提醒

    Returns:
        str: 任务内容
    """
    return "锻炼"

@status(task='睡觉',date=date)
def sleep():
    """提醒

    Returns:
        str: 任务内容
    """
    return "睡觉"

