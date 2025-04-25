import subprocess
import shlex

def run_applescript(script:str):
    subprocess.run(['osascript', '-e', script])


def run_shortcut(shortcut_name='',params:str=None):
    # 安全开启 放弃
    if params is None:
        run_applescript(f'''tell application "Shortcuts"
            run shortcut "{shortcut_name}"
        end tell''')
    else:
        run_applescript(f'''tell application "Shortcuts"
            run shortcut "{shortcut_name}" with {params}
        end tell''')

def display_dialog(title, text, button_text="OK"):
    # # --- 示例 ---
    # display_dialog("任务完成", "您的 Python 脚本已成功执行！")
    # display_dialog("用户输入", "请输入一些内容：", button_text="确认") # 这是一个简单的信息框，获取输入更复杂
    """使用 AppleScript 显示一个简单的对话框"""
    script = f'''
    display dialog "{text}" with title "{title}" buttons {{"{button_text}"}} default button "{button_text}"
    '''
    try:
        # 使用 shlex.quote 防止注入
        quoted_script = shlex.quote(script)
        subprocess.run(['osascript', '-e', script], check=True, capture_output=True, text=True)
        # 如果需要获取用户点击的按钮，可以解析 subprocess 的结果
        # result = subprocess.run(['osascript', '-e', script], check=True, capture_output=True, text=True)
        # print(result.stdout) # 例如 "button returned:OK"
    except subprocess.CalledProcessError as e:
        print(f"Error displaying dialog: {e}")
    except FileNotFoundError:
        print("Error: 'osascript' command not found. Ensure you are on macOS.")


import os
def get_commit_something(repo:str,commit:str):
    # git_commit_something
    os.system(f"cd /Users/zhaoxuefeng/GitHub/{repo};git add .; git commit -m '{commit}' --allow-empty")
