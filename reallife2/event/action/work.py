
from reallife2.utils.manager_utils import status, Date
date_c = Date()
date = date_c.date
time = date_c.time
# 同步预备池

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


@status(task="同步预备池",date=date,run_only=True)
def sync_ready_pool()->str:
    pathlib = ["/工程系统级设计/项目级别/数字人生/模拟资质认证/模拟资质认证.canvas",
               "/工程系统级设计/项目级别/数字人生/DigitalLife/DigitalLife.canvas",
               "/工程系统级设计/项目级别/自动化工作/coder/coder.canvas",]
    for path in pathlib:
        toReady(canvas_path="/Users/zhaoxuefeng/GitHub/obsidian/工作"+path,
                kanban_path ="/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md",)
    return 'success'


########


@status(task="同步就绪池",date=date,run_only=True)
def sync_order_pool()->str:
    url = "obsidian://open?vault=%E5%B7%A5%E4%BD%9C&file=%E4%BA%8B%E4%BB%B6%E7%9C%8B%E6%9D%BF%2F%E4%BA%8B%E4%BB%B6%E7%9C%8B%E6%9D%BF"
    
    kanban_path ="/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md"
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


##########

@status(task="同步执行池",date=date,run_only=True)
def sync_run_pool()->str:
    kanban_path ="/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md"
    
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




