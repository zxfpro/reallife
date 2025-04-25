
from kanban.core import Pool,Kanban

def runner2order(task:str,kanban_path:str):
    """从执行池  就绪池添加到 时间

    Args:
        kanban_path (str): 看板路径

    Returns:
        None: None
    """
    kanban = Kanban(kanban_path)
    kanban.pull()

    task_ = kanban.select_by_word(task)[0] # select_by_word_in
    kanban.pop(inputs=task_,by='description',pool=Pool.执行池)
    kanban.insert(text=task_,pool=Pool.就绪池)

    kanban.push()
    return 'success'

def main(task:str):
    runner2order(task,kanban_path ="/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md")
    return 'success'
    

if __name__ == "__main__":
    import sys
    multi_line_input = sys.stdin.read()
    # multi_line_input = '备案-新域名做域名备案'
    print(main(multi_line_input))

