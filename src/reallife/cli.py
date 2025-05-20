
from .workday_facade import WorkdayFacade
import sys
# 导入 WorkdayFacade 和 TaskManager，以及 CLI 函数
# from reallife.realLife__2 import WorkdayFacade, receive, complete, task_manager, list_tasks # Adjust import path

# 创建 WorkdayFacade 实例
workday_facade = WorkdayFacade()

def receive_task():
    """获取当前任务信息、状态和提示。不触发脚本执行。"""
    print("\n执行动作 1: receive (获取当前任务信息和提示)")
    # receive 函数只获取信息和提示，不触发脚本执行 (Automatic 脚本在 complete Todo 时执行)
    print(workday_facade.get_current_task_info())

def complete_task():
    """
    完成当前任务。
    如果当前任务是待办脚本任务，将触发脚本执行并根据结果更新状态。
    完成任务后，获取下一个任务信息并返回。
    """
    print("\n执行动作 2: complete (完成当前任务)")
    # complete 函数会完成当前任务，如果当前是待办 Automatic 任务，会触发脚本执行
    # 完成后，会显示下一个任务的信息
    print(workday_facade.complete_current_task())
    # list_tasks() # Optional: display updated list after each completion

def list_all_tasks():
     """列出所有任务及其状态"""
     print("\n--- 所有任务状态 ---")
     tasks_list = workday_facade.get_all_tasks_status()
     if not tasks_list:
         print("当前没有任务。")
         return
     for name, status in tasks_list:
         print(f"- {name}: {status}")
     print("---------------------")

def show_help():
    print("\n可用动作：")
    print("  1: 获取当前任务信息和提示 (receive)")
    print("  2: 完成当前任务 (complete)")
    print("  3: 列出所有任务状态 (list)")
    print("  41: 添加清晨任务")
    print("  42: 添加开工任务 (包含自动任务)")
    print("  43: 添加人工任务示例")
    print("  44: 添加收工任务")
    print("  45: 添加晚间任务")
    print("  51: 添加周末休息任务")
    print("  0: 清空所有任务")
    print("  help: 显示帮助信息")
    print("  quit/exit: 退出程序")

def main():
    print("欢迎使用任务管理 CLI 工具！")
    show_help()
    while True:
        print('\n-----------------------------')
        command = input("请输入动作名称 (或 'help', 'quit'): ").strip().lower()
        if command == '1':
            receive_task()
        elif command == '2':
            complete_task()
        elif command == '3':
            list_all_tasks()
        elif command == '41':
            print(workday_facade._morning_tasks())
        elif command == '42':
            print(workday_facade._start_work_tasks())
        elif command == '43':
            print(workday_facade.add_person_tasks())
        elif command == '44':
            print(workday_facade._finish_work_tasks())
        elif command == '45':
            print(workday_facade._evening_tasks())
        elif command == '51':
             print(workday_facade._rest())
        elif command == '0':
            workday_facade.clear()
        elif command == 'help':
            show_help()
        elif command in ['quit', 'exit']:
            print("退出程序。")
            break
        else:
            print(f"未知命令: {command}")
            show_help()

if __name__ == "__main__":
    main()