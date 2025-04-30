""" 系统工具箱 """

from datetime import datetime
import subprocess
import shlex
import os
import re
from typing import Optional
import functools
import requests

def git_commit_something(repo:str,commit:str):
    """提交git commit 

    Args:
        repo (str): 仓库
        commit (str): 提交信息
    """
    os.system(f"cd /Users/zhaoxuefeng/GitHub/{repo};git add .; \
              git commit -m '{commit}' --allow-empty")

def run_applescript(script:str)->str:
    """运行apple script 脚本

    Args:
        script (str): applescript 脚本

    Returns:
        str: 脚本的输出
    """
    result = subprocess.run(['osascript', '-e', script],capture_output=True,check=False)
    return result.stdout.decode().replace('\n','')

def run_shortcut(shortcut_name:str,params:str=None):
    """运行快捷指令

    Args:
        shortcut_name (str, optional): 快捷指令名称. Defaults to ''.
        params (str, optional): 参数. Defaults to None.

    Returns:
        str: 快捷指令的输出
    """
    # 安全开启 放弃
    if params is None:
        result = run_applescript(f'''tell application "Shortcuts"
            run shortcut "{shortcut_name}"
        end tell''')
    else:
        result = run_applescript(f'''tell application "Shortcuts"
            run shortcut "{shortcut_name}" with input "{params}"
        end tell''')
    return result


def display_dialog(title, text, button_text="OK",button_cancel = True):
    # # --- 示例 ---
    # display_dialog("任务完成", "您的 Python 脚本已成功执行！")
    # display_dialog("用户输入", "请输入一些内容：", button_text="确认") # 这是一个简单的信息框，获取输入更复杂
    """使用 AppleScript 显示一个简单的对话框"""
    if button_cancel:
        script = f'''
        display dialog "{text}" with title "{title}" buttons {{"cancel","{button_text}"}} \
            default button "{button_text}"
        '''
    else:
        script = f'''
        display dialog "{text}" with title "{title}" buttons {{"{button_text}"}} \
            default button "{button_text}"
        '''

    try:
        # 使用 shlex.quote 防止注入
        shlex.quote(script)
        result = subprocess.run(['osascript', '-e', script],
                                check=True, capture_output=True, text=True)
        # print(result.stdout)
        return result.stdout[16:-1]
    except subprocess.CalledProcessError as e:
        print(f"Error displaying dialog: {e}")
    except FileNotFoundError:
        print("Error: 'osascript' command not found. Ensure you are on macOS.")

def get_choice_from_applescript(prompt_text="请从下面的列表中选择一项：", list_title="请选择", options=None, default_option=None):
    """
    使用 AppleScript 显示一个列表选择框，并返回用户的选择。

    Args:
        prompt_text (str): 显示在列表上方的提示信息。
        list_title (str): 选择框窗口的标题。
        options (list): 供用户选择的字符串列表。
        default_option (str): 默认选中的项目。

    Returns:
        str: 用户选择的项目。
        None: 如果用户取消或发生错误。
    """
    if sys.platform != 'darwin':
        print("错误：此功能仅在 macOS 上可用。")
        return None

    if options is None:
        options = ["选项 A", "选项 B", "选项 C", "另一个选项"] # 默认选项

    # 将 Python 列表转换为 AppleScript 列表字符串: {"item1", "item2", ...}
    applescript_list = '{' + ', '.join([f'"{item}"' for item in options]) + '}'

    # 构建 AppleScript
    script = f'''
    try
        set myList to {applescript_list}
        set thePrompt to "{prompt_text}"
        set theTitle to "{list_title}"
        '''

    # 添加默认项（如果提供且有效）
    if default_option and default_option in options:
        script += f'set defaultChoice to {{"{default_option}"}}\n'
        script += f'set theChoice to choose from list myList with title theTitle with prompt thePrompt default items defaultChoice'
    else:
        script += f'set theChoice to choose from list myList with title theTitle with prompt thePrompt'

    script += f'''
        -- 检查用户是否点击了取消按钮
        if theChoice is false then
            error number -128 -- 引发标准取消错误
        else
            -- 返回选择的第一个项目 (choose from list 返回列表)
            return item 1 of theChoice
        end if
    on error number -128
        -- 捕获取消错误，可以返回特定值或让 Python 处理异常
         return "USER_CANCELLED" -- 返回一个特殊标记
         -- 或者你可以不处理，让 osascript 返回非零退出码
         -- error number -128
    end try
    '''

    try:
        # 不需要 shlex.quote
        result = subprocess.run(
            ['osascript', '-e', script],
            check=True,          # 如果 osascript 返回非零则抛出异常
            capture_output=True, # 捕获 stdout/stderr
            text=True,           # 将输出解码为文本
            encoding='utf-8'     # 指定编码
        )
        output = result.stdout.strip()
        if output == "USER_CANCELLED":
            print("用户取消了选择。")
            return None
        else:
            return output # 返回用户的选择
    except subprocess.CalledProcessError as e:
        # osascript 执行失败或返回错误码 (例如，如果我们在 AppleScript 中直接 error -128)
        # 检查 stderr 获取更多信息
        error_message = e.stderr.strip()
        if "-128" in error_message: # 检查是否是用户取消的标准错误代码
             print("用户取消了选择 (通过错误码捕获)。")
        else:
             print(f"执行 AppleScript 时出错: {e}")
             print(f"错误详情: {error_message}")
        return None
    except FileNotFoundError:
        print("错误: 'osascript' 命令未找到。请确保你在 macOS 上运行。")
        return None
    except Exception as e:
        print(f"发生意外错误: {e}")
        return None

def failed_safe():
    # 安全开启 放弃
    '''
    查询session状态
    如果 当前session 状态是 session
        放弃session
    否则
        pass
    结束
    '''
    run_shortcut(shortcut_name="安全停止")

def task_with_time(task_name:str,time:int=1):
    """计时任务

    Args:
        task_name (str): 任务名
        time (int, optional): 费用. Defaults to 1.
    """
    run_shortcut(shortcut_name="执行计时任务",params=f"{task_name}${time}")
    display_dialog("计时结束", "需要结束计时任务吗?",button_text="结束",button_cancel=False)

# 数据读取相关
def read_file(file_path: str) -> str:
    """
    读取文件内容
    :param file_path: 文件路径
    :return: 文件内容字符串
    """
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到")
        return ""

# 正则解析相关
def parse_execution_pool(text: str) -> Optional[str]:
    """
    使用正则表达式解析 "执行池" 内容
    :param text: 输入文本
    :return: 解析后的执行池内容
    """
    pattern = r'## 执行池\n(.+?)\n##'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        content = match.group(1).strip()
        formatted_content = '\n'.join([line.strip()
                                       for line in content.split('\n') if line.strip()])
        return formatted_content
    else:
        return None
# 正则解析相关
def parse_execution_jiangyou_pool(text: str) -> Optional[str]:
    """
    使用正则表达式解析 "执行池" 内容
    :param text: 输入文本
    :return: 解析后的执行池内容
    """
    pattern = r'## 酱油池\n(.+?)\n##'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        content = match.group(1).strip()
        formatted_content = '\n'.join([line.strip()
                                       for line in content.split('\n') if line.strip()])
        return formatted_content
    else:
        return None

class Date:
    """日期, 来控制系统时间

    Returns:
        object: 单例模式
    """
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self,date:str = None,time:str = None):
        # 只有第一次初始化时设置值，后续的初始化调用不会更改实例的值
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.date = date or datetime.today().strftime("%Y-%m-%d")
            self.time = time or datetime.today().strftime("%H:%M:%S")

## 其他

def status(task:str,date:str,run_only = False):
    """执行任务并记录执行状态, 如果已经执行了则不再执行(每日)

    Args:
        task (str): 任务名称
        date (str): 2019-12-12

    Returns:
        str: '是否成功'
    """
    def outer_packing(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            response = requests.get(
                f"http://101.201.244.227:8000/action/{task}/{date}/status",timeout=20)
            if response.json().get('status') == '未执行':
                result = func(*args, **kwargs)
            else:
                result = None
            if run_only:
                response = requests.post(
                f"http://101.201.244.227:8000/action/{task}/{date}/execute",timeout=20)
            return result
        return wrapper
    return outer_packing




def push_task(task:str, date:str):
    """推任务上去

    Args:
        task (str): 任务名
        date (str): 日期
    """
    requests.post(
        f"http://101.201.244.227:8000/action/{task}/{date}/execute",timeout=20)
    return 'success'

def reset_task(task:str,date:str)->str:
    """重置任务

    Args:
        task (str): 任务名
        date (str): 日期

    Returns:
        str: 系统消息
    """
    requests.post(
        f"http://101.201.244.227:8000/action/{task}/{date}/reset",timeout=20)
    return 'success'

def reset_tasks(date:str):
    """重置多任务

    Args:
        date (str): 日期
    """
    for task in ['同步进程池','同步预备池','同步就绪池','同步执行池',]:
        reset_task(task,date)


def create_func(task:str,date:str)->object:
    """创建特定对象

    Args:
        task (str): 任务
        date (str, optional): 日期. Defaults to date.

    Returns:
        object: 状态函数
    """
    @status(task=task,date=date)
    def func_():
        """提醒

        Returns:
            str: 任务内容
        """
        return task
    return func_
