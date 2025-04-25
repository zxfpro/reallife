"""
"""

from grapherz.canvas.core import Canvas,Color
from kanban.core import Pool,Kanban

def encode(i,project_name):
    return project_name+'-'+i

def save_in_pauses(i,pauses):
    for pause in pauses:
        if i.get('text') in pause:
            return True
    return False

def toReady(canvas_path:str,kanban_path:str):
    project_name = canvas_path.rsplit('/',2)[-2] 

    canvas = Canvas(file_path=canvas_path)
    kanban = Kanban(kanban_path)
    kanban.pull()
    pauses = kanban.get_tasks_in(pool=Pool.阻塞池)
    readys = kanban.get_tasks_in(pool=Pool.预备池)

    nodes = [i.get('text') or '' for i in canvas.select_by_color(Color.yellow,type='node') if not save_in_pauses(i,pauses=pauses)]
    for i in nodes:
        if i not in readys:
            kanban.insert(text=encode(i,project_name),pool=Pool.预备池)
    kanban.push()

    return 'success'

def main(path):
    toReady(canvas_path="/Users/zhaoxuefeng/GitHub/obsidian/工作"+path,
            kanban_path ="/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md",)
    return 'success'
    
if __name__ == "__main__":
    import sys
    multi_line_input = sys.stdin.read()
    print(main(multi_line_input))
