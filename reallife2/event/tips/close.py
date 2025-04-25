
from reallife2.utils.manager_utils import status, Date

date_c = Date()
date = date_c.date

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

