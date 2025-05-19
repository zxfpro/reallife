# task_func__1.py



from .execution_strategy import PersonTaskExecutionStrategy, PromptTaskExecutionStrategy, ScriptTaskExecutionStrategy,TaskExecutionStrategy
from .task_state import TaskState, TodoState
from .task_manager import TaskManager,Task

# reallife__1.py
# from .task_func__1 import TaskManager, PromptTaskExecutionStrategy, ScriptTaskExecutionStrategy, TodoState, InProgressState, CompletedState

# Global TaskManager instance (for simplicity in this example)
task_manager = TaskManager()

# Workday Facade
class WorkdayFacade:
    """工作日外观类，为日常任务处理提供统一接口"""
    def __init__(self):
        pass

    def clear(self):
        task_manager.clear()

    def _morning_tasks(self) -> str:
        """清晨任务"""
        task_manager.add_task("记录灵感")
        task_manager.add_task("记录体重")
        task_manager.add_task("跑步")
        task_manager.add_task("记录吃了什么")
        task_manager.add_task("洗漱护肤")
        task_manager.add_task("收拾家与锻炼")
        return "清晨任务已添加"

    def _start_work_tasks(self) -> str:
        """开工任务"""
        task_manager.add_task("上班打卡", task_type="prompt")
        task_manager.add_task("同步体重",task_type = "script",script_code = None)
        task_manager.add_task("汇总到预备池", task_type="script", script_code=None)
        task_manager.add_task("同步到就绪池", task_type="script", script_code=None)
        task_manager.add_task("调整优先级", task_type="prompt")
        task_manager.add_task("同步到执行池", task_type="script", script_code=None)
        task_manager.add_task("同步到日历", task_type="script", script_code=None)
        task_manager.add_task("同步到备忘录", task_type="script", script_code=None)
        task_manager.add_task("倒水", task_type="prompt")
        task_manager.add_task("写下灵感", task_type="prompt")
        task_manager.add_task("跟进阻塞池", task_type="prompt")
        return "开工任务已添加"



    def _finish_work_tasks(self) -> str:
        """收工任务"""
        task_manager.add_task("同步体重 (收工)", task_type="script", script_code=None)
        task_manager.add_task("同步到备忘录", task_type="script", script_code=None)
        task_manager.add_task("检查和收集咨询", task_type="prompt")
        task_manager.add_task("检查是否仍在禅模式", task_type="prompt")
        task_manager.add_task("检测git提交", task_type="prompt")
        task_manager.add_task("下班打卡", task_type="prompt")
        task_manager.add_task("倒水", task_type="prompt")
        return "收工任务已添加"

    def _evening_tasks(self) -> str:
        """晚间休息任务"""
        task_manager.add_task("整理家里和猫猫", task_type="prompt")
        task_manager.add_task("晚上洗漱,刷牙,护肤", task_type="prompt")
        task_manager.add_task("锻炼", task_type="prompt")
        task_manager.add_task("睡觉", task_type="prompt")
        return "晚间任务已添加"
    
    def _rest(self) -> str:
        """晚间休息任务"""
        task_manager.add_task("周末", task_type="prompt")
        task_manager.add_task("查看备忘录", task_type="prompt")
        task_manager.add_task("锻炼", task_type="prompt")
        task_manager.add_task("玩游戏", task_type="prompt")
        return "晚间任务已添加"
    
    

    def get_current_task_info(self):
         """
         获取当前任务的名称、状态和提示。
         此方法不触发脚本执行。
         """
         current_task = task_manager.get_current_sequential_task()
         if current_task:
             # Call request() to get the handle message/prompt from the current state
             prompt = current_task.request()
             return f"当前任务：{current_task.name} ({current_task.get_status()})\n提示: {prompt}"
         else:
             return "所有任务已完成！"

    def complete_current_task(self) -> str:
        """
        完成当前按顺序应执行的任务。
        如果当前任务是待办的脚本任务，将在此处触发脚本执行。
        """
        return task_manager.complete_current_task()

    def get_all_tasks_status(self):
         """获取所有任务的列表和状态"""
         return task_manager.get_task_list()


# --- CLI Interface Functions ---
# These functions interact with the WorkdayFacade
def receive():
    """获取当前任务信息、状态和提示。不触发脚本执行。"""
    return workday_facade.get_current_task_info()

def complete():
    """
    完成当前任务。
    如果当前任务是待办脚本任务，将触发脚本执行。
    完成任务后，获取下一个任务信息并返回。
    """
    # print("尝试完成当前任务...")
    complete_message = workday_facade.complete_current_task()
    # print(f"完成结果: {complete_message}")

    # 获取下一个任务信息（或更新后的当前任务信息）
    next_task_info = receive() # Call receive to get info about the new current task (or the completed one)
    return next_task_info

def list_tasks():
     """列出所有任务及其状态"""
    #  print("--- 所有任务状态 ---")
     tasks_list = workday_facade.get_all_tasks_status()
     if not tasks_list:
        #  print("当前没有任务。")
         return
     for name, status in tasks_list:
         print(f"- {name}: {status}")
     print("---------------------")

