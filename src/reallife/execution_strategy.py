from .abstra import TaskExecutionStrategy

from appscriptz.main import APPManager
import requests

apps = APPManager()

def sync_weight(date)->str:
    """
    同步体重
    """

    url = f"http://101.201.244.227:8000/weight/{date}"
    response = requests.get(url)
    result = response.json().get('weight')
    x = f"""---
番茄: 14
体重: {result}
---
"""

    with open(self.main_path + f'/日记/{date}.md','a') as f:
        f.write(x)
    return 'success'

# 具体策略：提示任务执行策略 (人工执行)
class PromptTaskExecutionStrategy(TaskExecutionStrategy):
    def execute(self, task_context):
        # 对于 Prompt 任务，execute 方法主要被 State 调用以获取提示
        # handle() 方法是 State 模式中获取提示的地方
        # print(f"Inside PromptTaskExecutionStrategy.execute for '{task_context.name}'. Called by State.")
        # 返回状态提供的提示
        return task_context._state.handle(task_context)
    

# 具体策略：自动任务执行策略 (电脑自动执行)
class AutomaticTaskExecutionStrategy(TaskExecutionStrategy):
    def execute(self, task_context):
        print(f"Inside AutomaticTaskExecutionStrategy.execute for '{task_context.name}'. Running automatic task...")
        try:
            # 这里模拟自动任务的执行逻辑
            # 实际应用中，这里会调用外部服务、执行脚本、处理数据等
            # if task_context.script_code:
            if task_context.name == '同步体重':
                print('已同步体重')
            elif task_context.name == '汇总到预备池':
                print('已汇总到预备池')
            elif task_context.name == '同步到就绪池':
                print('已同步到就绪池')
            elif task_context.name == '同步到执行池':
                print('已同步到执行池')
            elif task_context.name == '同步到日历':
                print('已同步到日历')
            elif task_context.name == '同步到备忘录':
                print('已同步到备忘录')
                apps.memorandum2notes('已同步到备忘录')
            elif task_context.name == '同步体重 (收工)':
                print('同步体重 (收工)')
            elif task_context.name == '同步到备忘录 (收工)':
                print("同步到备忘录 (收工)")
                apps.memorandum2notes('同步到备忘录 (收工)')

            if task_context.script_code:
                # 模拟执行脚本
                print(f"Automatic task '{task_context.name}' executed successfully.")
                # 模拟执行成功
                return {"status": "success", "message": f"自动任务 '{task_context.name}' 执行完毕。"}
            else:
                print(f"Automatic task '{task_context.name}' has no script code.")
                # 模拟执行成功 (没有代码也算执行成功)
                return {"status": "success", "message": f"自动任务 '{task_context.name}' 没有提供脚本代码，但标记为完成。"}
        except Exception as e:
            print(f"Automatic task '{task_context.name}' execution failed: {e}")
            # 模拟执行失败
            return {"status": "failure", "message": f"自动任务 '{task_context.name}' 执行失败：{e}"}
