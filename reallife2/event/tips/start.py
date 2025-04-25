
from reallife2.utils.manager_utils import status, Date

date_c = Date()
date = date_c.date
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

