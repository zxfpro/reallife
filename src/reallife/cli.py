
import sys
from .workday_facade import WorkdayFacade,receive,complete, list_tasks
from .task_manager import 
workday_facade = WorkdayFacade()


def show_help():
    print("\n可用动作：")
    print("  1: 获取当前任务信息和提示 (不触发脚本执行)")
    print("  2: 完成当前任务 (待办脚本任务会在此处执行，然后显示下一个任务)")
    print("  3: 列出所有任务状态")
    print("  help: 显示帮助信息")
    print("  quit/exit: 退出程序")

def main():
    print("欢迎使用简单的 CLI 工具！")
    show_help()
    while True:
        print('\n-----------------------------')
        command = input("请输入动作名称 (或 'help', 'quit'): ").strip().lower()
        if command == '1':
            receive()
        elif command == '2':
            complete()
        elif command == '3':
            list_tasks()
        elif command == '3':
            list_tasks()
        elif command == '41':
            workday_facade._morning_tasks()
        elif command == '42':
            workday_facade._start_work_tasks()
        elif command == '43':
            lists = ['任务1','任务2','任务3','任务4']
            for i in lists:
                task_manager.add_task(i,task_type='person')
        elif command == '44':
            workday_facade._finish_work_tasks()
        elif command == '45':
            workday_facade._evening_tasks()

        elif command == '51':
            workday_facade._rest()

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
