""" 执行任务 """
from llmada import BianXieAdapter
from kanban.core import Pool,Kanban
from grapherz.canvas.core import Canvas,Color
from promptlibz.work import JudgeType
from .utils import failed_safe, task_with_time, git_commit_something, display_dialog, get_choice_from_applescript
from .action import KanBanManager, KANBAN_PATH, WORK_CANVAS_PATH

import re

def extract_type_code(text: str)->str:
    """从文本中提取python代码

    Args:
        text (str): 输入的文本。

    Returns:
        str: 提取出的python文本
    """
    pattern = r'```type([\s\S]*?)```'
    matches = re.findall(pattern, text)
    return matches[0].replace('\n','')

def judge_type(task:str):
    """判断任务类型

    Args:
        task (str): 任务
    """

    llm = BianXieAdapter()
    llm.set_model('gpt-4.1-mini')
    prompt = JudgeType.prompt.format(task=task)
    completion = llm.product(prompt)
    return extract_type_code(completion)

def edit_coder(task:str):
    """编写代码

    Args:
        task (str): 任务
    """

    # 是否创建项目
    create_proj = False
    display_dialog("编写代码",f"是否创建新项目: {task}",button_text="开始",button_cancel=False)
    create_proj = display_dialog("编写代码",f"是否创建新项目: ",button_text="create",button_cancel=True)
    if create_proj == 'create':
        display_dialog("创建项目","1. pypi查重 \n  2. obsidian创建Reader | Docs \n \
                       3创建github仓库",button_text="确认",button_cancel=False)
        display_dialog("创建项目","初始化 uv init and 修改解释器 \
                       mkdocs new .  update  文档推送  创建文件夹,\
                       测试文件等  \
                       uv build publish  ",button_text="确认", button_cancel=False)
    print(task,'task')
    # TODO
    lst = ['coderTools','grapher','kanban']

    get_choice_from_applescript()
    all_options = ['coderTools','grapher','kanban','llmada','networkx','ob_ragtools','obsidian','promptlib',
                   'pypidoctor','readerLLamaIndex','reallife','tools','aiworker']
    choice = get_choice_from_applescript(
        prompt_text="请选择作为工作区的仓库:",
        list_title="工作区",
        options=all_options,
        default_option="kanban"
    )
    if choice:
        select = choice
    else:
        select = None
        raise Exception('选择失效')
    #
    display_dialog("编码与练习","基础逻辑",button_text="确认")
    task_with_time(task_name = task,time=40)
    display_dialog("编码与练习","测试与测试用例",button_text="确认")
    task_with_time(task_name = task,time=30)
    display_dialog("编码与练习","整理代码,注释,格式,文档与发布",button_text="确认")
    task_with_time(task_name = task,time=20)
    display_dialog("编码与练习","环境与推送新版本",button_text="确认")
    task_with_time(task_name = task,time=10)
    # 仓库$编写目标
    git_commit_something(select,task)
    failed_safe()

def test_and_study(task:str):
    """实验与学习

    Args:
        task (str): 任务
    """
    # 实验与学习
    display_dialog("实验与学习",f"请打开飞书会议, 标题为{task}",button_text="确认",button_cancel=False)
    task_with_time(task_name = task,time=60)
    display_dialog("实验与学习","自我审视+ 反思 + 分析笔记",button_text="确认",button_cancel=False)
    failed_safe()

def clean_and_update(task:str):
    """整理与优化

    Args:
        task (str): 任务
    """
    display_dialog("整理与优化",f"是否可以开始整理与优化: {task}",button_text="可以",button_cancel=False)
    task_with_time(task_name = task,time=20)
    failed_safe()

def design(task:str):
    """设计

    Args:
        task (str): 任务名
    """
    display_dialog("设计",f"准备开始设计: {task}",button_text="开始",button_cancel=False)
    task_with_time(task_name = task,time=60)
    git_commit_something("obsidian",task)
    failed_safe()

def meeting_and_talk(task:str):
    """开会与对齐

    Args:
        task (str): 任务名
    """
    display_dialog("开会与对齐",f"准备开会与对齐: {task}",button_text="开始",button_cancel=False)
    task_with_time(task_name = task,time=60)
    failed_safe()

def task_complete(task):

    # 任务已完成
    # multi_line_input = "真实人生-将对应的执行池内容添加到完成池"

    """
     script/kanban_manager_2over_function.py
    任务$canvas_path
     script/kanban_manager_2over.py
    """
    project_paths = WORK_CANVAS_PATH
    # task = "真实人生-将对应的执行池内容添加到完成池"
    project = task.split('-',1)[0]
    now_project_path = None
    for project_path in project_paths:
        if project == project_path.split('/')[-2]:
            now_project_path = project_path

    kbm = KanBanManager(kanban_path=KANBAN_PATH,pathlib=WORK_CANVAS_PATH)
    print('now_project_path',now_project_path)
    if now_project_path:
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
    kbm = KanBanManager(kanban_path=KANBAN_PATH,pathlib=WORK_CANVAS_PATH)
    kbm.sync_run2order(task)
