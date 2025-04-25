
from reallife2.utils.manager_utils import status, Date

date_c = Date()
date = date_c.date

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
