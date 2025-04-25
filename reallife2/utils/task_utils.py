from utils import get_commit_something
from utils import run_applescript,run_shortcut
from utils import display_dialog
# # git_commit_obsidian
# def git_commit_obsidian(commit:str):
#     os.system(f"cd /Users/zhaoxuefeng/GitHub/obsidian;git add .; git commit -m '{commit}' --allow-empty")



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
    run_applescript(f'''tell application "Shortcuts"
        run shortcut "安全停止"
    end tell''')


    
def task_with_time(task_name:str,time:int=1):
    # 记时任务 3费
    display_dialog("开始", "您的 Python 脚本已成功执行！")
    # Start Session 目标 with category 通用
    run_shortcut(shortcut_name="开始 session",params='你是谁')
    # 执行完成提示
    display_dialog("完成", "您的 Python 脚本已成功！")

if __name__ == "__main__":
    print(task_with_time(task_name='你好',time=1))



