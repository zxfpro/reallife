import requests
import functools

from datetime import datetime
class Date:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # 只有第一次初始化时设置值，后续的初始化调用不会更改实例的值
        if not hasattr(self, 'initialized'):
            self.initialized = True
            # self.date = datetime.today().strftime("%Y-%m-%d")
            self.date = '2025-02-12'
            self.time = datetime.today().strftime("%H:%M:%S")

def status(task:str,date:str,run_only = False):
    """执行任务并记录执行状态, 如果已经执行了则不再执行(每日)

    Args:
        task (str): 任务名称
        date (str): 2019-12-12

    Returns:
        str: '是否成功'
    """
    def outer_packing(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            response = requests.get("http://101.201.244.227:8000/action/{task}/{date}/status".format(task=task,date=date))
            if response.json().get('status') == '未执行':
                result = func(*args, **kwargs)
            else:
                result = None
            if run_only:
                response = requests.post("http://101.201.244.227:8000/action/{task}/{date}/execute".format(task=task,date=date))
            return result
        return wrapper
    return outer_packing




def push_task(task:str, date:str):
    """推任务上去

    Args:
        task (str): 任务名
        date (str): 日期
    """
    response = requests.post("http://101.201.244.227:8000/action/{task}/{date}/execute".format(task=task,date=date))


def reset_task(task:str,date:str):
    response = requests.post("http://101.201.244.227:8000/action/{task}/{date}/reset".format(task=task,date=date))

def reset_tasks(task:str,date:str):
    [reset_task(task,date) 
     for task in [
        '同步进程池',
        '同步预备池',
        '同步就绪池',
        '同步执行池',
    ]]

