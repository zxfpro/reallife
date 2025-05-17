import sys

from reallife.realLife__1 import receive,complete, WorkdayFacade

workday_facade = WorkdayFacade(1,2)
workday_facade._start_work_tasks()

def receive_1():
    print("执行动作 receive")
    print(receive())

def complete_1():
    print("执行动作 complete")
    x = input("完成:")
    print(complete(x))

def show_help():
    print("可用动作：")
    print("  1: 执行动作 receive")
    print("  2: 执行动作 complete")
    print("  help: 显示帮助信息")
    print("  quit/exit: 退出程序")

def main():
    print("欢迎使用简单的 CLI 工具！")
    show_help()

    while True:
        print('-----------------------------')
        command = input("请输入动作名称 (或 'help', 'quit'): ").strip().lower()

        if command == '1':
            receive_1()
        elif command == '2':
            complete_1()
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