"""提供一些带状态的消息"""


from reallife2.utils.manager_utils import status, Date

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
