
from kanban.core import Pool,Kanban
from grapherz.canvas.core import Canvas,Color

def runner2over(task:str,kanban_path:str,canvas_path:str):
    """从执行池添加到完成池
    1 将task从执行池添加到完成池
    2 将canvas 中的颜色变绿
    Args:
        kanban_path (str): 看板路径

    Returns:
        None: None
    """
    kanban = Kanban(kanban_path)
    kanban.pull()
    task = task.split('-',1)[-1]
    if len(kanban.get_task_by_word(task,pool=Pool.执行池)) == 0:
        kanban.insert(text=task,pool=Pool.完成池)
        kanban.push()
        return 'failed'
        
    task_ = kanban.get_task_by_word(task,pool=Pool.执行池)[0]
    kanban.pop(text=task_,pool=Pool.执行池)
    kanban.insert(text=task_,pool=Pool.完成池)
    
    # and
    canvas = Canvas(file_path=canvas_path)
    tasks = canvas.select_nodes_by_text(task)
    try:
        tasks[0].color = Color.green.value
    except IndexError as e:
        return f'error: {e}'
    canvas.to_file(canvas_path)
    kanban.push()
    return 'success'

def main(taskandcanvas_path:str):
    task,canvas_path = taskandcanvas_path.split("$")
    canvas_path = canvas_path.replace('\n','')
    runner2over(task,
                kanban_path ="/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md",
                canvas_path ="/Users/zhaoxuefeng/GitHub/obsidian/工作"+canvas_path)
    return 'success'
    
if __name__ == "__main__":
    import sys
    multi_line_input = sys.stdin.read()
    # multi_line_input = "备案-新域名做域名备案$/工程系统级设计/项目级别/数字人生/模拟资质认证/模拟资质认证.canvas\n"
    print(main(multi_line_input))
