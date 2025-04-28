""" 执行任务 """
from llmada import BianXieAdapter
from kanban.core import Pool,Kanban
from grapherz.canvas.core import Canvas,Color
from promptlibz.work import JudgeType
from .utils import failed_safe, task_with_time, get_commit_something, display_dialog
from .action import KanBanManager

def judge_type(task:str):
    """判断任务类型

    Args:
        task (str): 任务
    """

    llm = BianXieAdapter()
    llm.set_model('gpt-4.1-mini')
    prompt = JudgeType.prompt.format(task=task)
    completion = llm.product(prompt)
    return completion

def edit_coder(task:str):
    """编写代码

    Args:
        task (str): 任务
    """

    # 是否创建项目
    create_proj = False

    if create_proj:
        failed_safe()
        display_dialog("创建项目","1. pypi查重 \n  2. obsidian创建Reader | Docs \n \
                       3创建github仓库",button_text="确认")
        display_dialog("创建项目","初始化 uv init and 修改解释器 \
                       mkdocs new .  update  文档推送  创建文件夹,\
                       测试文件等  \
                       uv build publish  ",button_text="确认")



    # _create_project(task)
    # TODO
    lst = ['coderTools','grapher','kanban']
    select = 'kanban'
    #
    failed_safe()
    display_dialog("编码与练习","基础逻辑",button_text="确认")
    task_with_time(task_name = task,time=40)
    display_dialog("编码与练习","测试与测试用例",button_text="确认")
    task_with_time(task_name = task,time=30)
    display_dialog("编码与练习","整理代码,注释,格式,文档与发布",button_text="确认")
    task_with_time(task_name = task,time=20)
    display_dialog("编码与练习","环境与推送新版本",button_text="确认")
    task_with_time(task_name = task,time=10)
    # 仓库$编写目标
    get_commit_something(select,task)

def test_and_study(task:str):
    """实验与学习

    Args:
        task (str): 任务
    """
    # 实验与学习

    failed_safe()

    display_dialog("实验与学习",f"请打开飞书会议, 标题为{task}",button_text="确认")
    task_with_time(task_name = task,time=60)
    display_dialog("实验与学习","实验记录 + 录屏 + 存根",button_text="确认")
    display_dialog("实验与学习","录音 + 微信语音",button_text="确认")
    display_dialog("实验与学习","自我审视 +  面试录音 + 反思 + 分析笔记",button_text="确认")

def clean_and_update(task:str):
    """整理与优化

    Args:
        task (str): 任务
    """
    failed_safe()
    task_with_time(task_name = task,time=20)

def design(task:str):
    """设计

    Args:
        task (str): 任务名
    """
    failed_safe()
    task_with_time(task_name = task,time=60)
    get_commit_something("obsidain",task)


def meeting_and_talk(task:str):
    """开会与对齐

    Args:
        task (str): 任务名
    """
    # 开会与对齐
    failed_safe()
    task_with_time(task_name = task,time=3)

def task_finish(task):

    # 任务已完成
    # multi_line_input = "真实人生-将对应的执行池内容添加到完成池"


    """
     script/kanban_manager_2over_function.py
    任务$canvas_path
     script/kanban_manager_2over.py
    """
    project_paths = ["/工程系统级设计/项目级别/数字人生/模拟资质认证/模拟资质认证.canvas",
                    "/工程系统级设计/项目级别/数字人生/DigitalLife/施工安排.canvas",
                    "/工程系统级设计/项目级别/autoworker/施工安排.canvas",
                    "/工程系统级设计/项目级别/真实人生/施工安排.canvas"]
    # task = "真实人生-将对应的执行池内容添加到完成池"
    project = task.split('-',1)[0]
    now_project_path = None
    for project_path in project_paths:
        if project == project_path.split('/')[-2]:
            now_project_path = project_path

    kbm = KanBanManager()
    kbm.sync_run2over(task,canvas_path=now_project_path)

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

    # taskandcanvas_path = "备案-新域名做域名备案$/工程系统级设计/项目级别/数字人生/模拟资质认证/模拟资质认证.canvas\n"

    canvas_path = now_project_path.replace('\n','')
    runner2over(task,
                kanban_path ="/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md",
                canvas_path ="/Users/zhaoxuefeng/GitHub/obsidian/工作"+canvas_path)
    return 'success'

##########


def task_failed(task):
    # 任务未完成
    """
     script/kanban_manager_runner2order.py
    """
    kbm = KanBanManager()
    kbm.sync_run2order(task)
