from reallife2.utils.manager_utils import status, Date

date_c = Date()
date = date_c.date
time = date_c.time
# 同步预备池
from reallife.status.news import sync_news_func
from reallife.status.notes import sync_notes_function






@status(task="收集资讯",date=date,run_only=True)
def sync_news()->str:
    sync_news_func(date)
    return 'success'

@status(task="同步备忘录",date=date,run_only=True)
def sync_note()->str:
    sync_notes_function()
    return 'success'
