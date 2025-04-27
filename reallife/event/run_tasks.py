from ..utils.utils import failed_safe, task_with_time, get_commit_something
from ..utils.utils import display_dialog

def judge_type(task):
    return "设计"

def _create_project(target):
    # 创建项目
    failed_safe()
    display_dialog("创建项目",f"pypi中查找名称(不重名),  obsidian下创建对应的Reader and Docs 创建github仓库, 拉取. 获取脚本",button_text="确认")
    display_dialog("创建项目",f"初始化 uv init and 修改解释器  mkdocs new .  update  文档推送  创建文件夹, 测试文件等  uv build publish  ",button_text="确认")

def edit_coder(task):
    # 编写代码
    
    # 是否创建项目
    # _create_project(task)

    lst = ['coderTools','grapher','kanban']
    select = 'kanban'

    failed_safe()
    #编写代码基础逻辑:-> 编写目标
    display_dialog("2",f"编写代码基础逻辑:-> 编写目标",button_text="确认")
    task_with_time(task_name = task,time=1)
    # 编写目标 整理代码 UseCase 注释:->
    display_dialog("2",f"编写目标 整理代码 UseCase 注释:->",button_text="确认")
    task_with_time(task_name = task,time=1)
    # 编写目 编写测试用例:->
    display_dialog("2",f"编写目 编写测试用例:->",button_text="确认")
    task_with_time(task_name = task,time=1)
    # 编写相关文档:->编写目标
    display_dialog("2",f"编写相关文档:->编写目标",button_text="确认")
    task_with_time(task_name = task,time=1)
    # 修改并推送版本:->编写目标
    display_dialog("2",f"修改并推送版本:->编写目标",button_text="确认")
    task_with_time(task_name = task,time=1)
    # 仓库$编写目标
    get_commit_something(select,task)

def test_and_study(task):
    # 实验与学习

    failed_safe()

    display_dialog("录屏",f"请打开飞书会议, 标题为{task}",button_text="确认")

    task_with_time(task_name = task,time=3)

    display_dialog("1","实验记录 + 录屏 + 存根",button_text="确认")

    display_dialog("1","录音 + 微信语音",button_text="确认")

    display_dialog("1","自我审视 +  面试录音 + 反思 + 分析笔记",button_text="确认")



def clean_and_update(task):
    # 整理yu优化
    failed_safe()
    task_with_time(task_name = task,time=1)


def design(task):
    # 设计
    failed_safe()
    task_with_time(task_name = task,time=3)
    get_commit_something("obsidain",task)


def meeting_and_talk(task):
    # 开会与对齐
    failed_safe()
    task_with_time(task_name = task,time=3)

def task_finish(task):
    # 任务已完成
    """
     script/kanban_manager_2over_function.py
    任务$canvas_path
     script/kanban_manager_2over.py
    """
###########

def main(task):
    project_paths = ["/工程系统级设计/项目级别/数字人生/模拟资质认证/模拟资质认证.canvas",
                    "/工程系统级设计/项目级别/数字人生/DigitalLife/施工安排.canvas",
                    "/工程系统级设计/项目级别/autoworker/施工安排.canvas",
                    "/工程系统级设计/项目级别/真实人生/施工安排.canvas"]

    project = task.split('-',1)[0]
    for project_path in project_paths:
        if project == project_path.split('/')[-2]:
            return project_path
    return 'no'

    
if __name__ == "__main__":
    import sys
    multi_line_input = sys.stdin.read()
    # multi_line_input = "真实人生-将对应的执行池内容添加到完成池"
    print(main(multi_line_input))


##########
    # 任务$canvas_path

    kbm = KanBanManager(kanban_path="")
    kbm.sync_run2over(task)

#########

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


##########


def task_failed(task):
    # 任务未完成
    """
     script/kanban_manager_runner2order.py
    """
    kbm = KanBanManager(kanban_path="")
    kbm.sync_run2order(task)


from .action import KanBanManager
