
from kanban.core import Pool,Kanban

def order2runner(kanban_path:str):
    """从就绪池添加到执行池 时间

    Args:
        kanban_path (str): 看板路径

    Returns:
        None: None
    """
    kanban = Kanban(kanban_path)
    kanban.pull()

    
    tasks = kanban.get_tasks_in(Pool.就绪池)
    all_task_time = 0
    for task in tasks:
        task_time = int(task.split(' ')[0][:-1])

        if all_task_time + task_time <=14:
            all_task_time += task_time
            kanban.pop(text=task,pool=Pool.就绪池)
            kanban.insert(text=task,pool=Pool.执行池)

        elif all_task_time < 8:
            pass
    kanban.push()
    return 'success'

def main():
    order2runner(kanban_path ="/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md")
    return 'success'
    
if __name__ == "__main__":
    main()
