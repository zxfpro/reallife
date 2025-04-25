from kanban.core import Pool,Kanban

def add_tips(task:str,kanban_path:str):
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

    kanban.insert(text=task,pool=Pool.酱油池)
    kanban.push()
    return 'success'

def main(task:str):
    add_tips(task,kanban_path ="/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md",)
    return 'success'
    
if __name__ == "__main__":
    import sys
    multi_line_input = sys.stdin.read()
    # multi_line_input = "备案-新域名做域名备案$/工程系统级设计/项目级别/数字人生/模拟资质认证/模拟资质认证.canvas\n"
    print(main(multi_line_input))
