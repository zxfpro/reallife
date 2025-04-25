
from kanban.core import Pool,Kanban

def ready2order(kanban_path:str):
    """从预备池添加内容到就绪池, 添加时间, 去重

    Args:
        kanban_path (str): 看板路径

    Returns:
        None: None
    """
    kanban = Kanban(kanban_path)
    kanban.pull()

    def give_a_task_time(task:str)->str:
        return "2P " + task
    
    tasks = kanban.get_tasks_in(Pool.预备池)
    order_tasks = kanban.get_tasks_in(Pool.就绪池)
    orders = ' '.join(order_tasks)
    for task in tasks:
        kanban.pop(text = task,pool = Pool.预备池)
        if task not in orders:
            task_ = give_a_task_time(task)
            kanban.insert(text=task_,pool=Pool.就绪池)

    kanban.push()
    return 'success'

def main():
    ready2order(kanban_path ="/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md")
    return 'success'
    
if __name__ == "__main__":
    main()
