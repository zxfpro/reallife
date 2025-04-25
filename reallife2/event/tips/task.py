
from reallife2.utils.manager_utils import status, Date

date_c = Date()
date = date_c.date

# tasks
@status(task='写下灵感',date=date)
def write_thinking():
    """提醒

    Returns:
        str: 任务内容
    """
    return "写下灵感"


