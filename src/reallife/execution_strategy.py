from .abstra import TaskExecutionStrategy


# 具体策略：提示任务执行策略
class PromptTaskExecutionStrategy(TaskExecutionStrategy):
    def execute(self, task_context):
        # Prompt 任务的执行就是返回状态提示，但这个方法现在主要由 State 调用
        # handle() 方法是 State 模式中获取提示的地方
        print(f"Inside PromptTaskExecutionStrategy.execute for '{task_context.name}'. This is called by State.")
        return task_context._state.handle(task_context)

# 具体策略：脚本任务执行策略
class ScriptTaskExecutionStrategy(TaskExecutionStrategy):
    def execute(self, task_context):
        print(f"Inside ScriptTaskExecutionStrategy.execute for '{task_context.name}'. Running script...")
        print('\n\n')
        print(task_context,'task_context') # <__main__.Task object at 0x102bdfd90> task_context
        print(task_context.name,'ccvvv')
        try:
            # 注意：安全问题！这里只是示例，实际应用中需要谨慎处理

            if task_context.name == '汇总到预备池':
                pass
            elif task_context.name == '同步到就绪池':
                pass
            elif task_context.name == '同步到执行池':
                pass
            elif task_context.name == '同步到日历':
                pass
            elif task_context.name == '同步到备忘录':
                pass
            elif task_context.name == '同步体重':
                pass


            if task_context.script_code:
                # Execute the script code
                exec(task_context.script_code)
                return f"脚本任务 '{task_context.name}' 执行完毕。"
            else:
                 return f"脚本任务 '{task_context.name}' 没有提供脚本代码。"
        except Exception as e:
            # The state transition on failure would need to be handled by the caller (e.g., TodoState.complete)
            # Or we could return a special error message and let the State decide how to handle it.
            # For simplicity now, just return the error message.
            return f"脚本任务 '{task_context.name}' 执行失败：{e}"



class PersonTaskExecutionStrategy(TaskExecutionStrategy):
    def execute(self, task_context):
        print(f"Inside PersonTaskExecutionStrategy.execute for '{task_context.name}'. Running script...")
        print('\n\n')
        print(task_context,'task_context') # <__main__.Task object at 0x102bdfd90> task_context
        print(task_context.name,'ccvvv')
        try:
            # 注意：安全问题！这里只是示例，实际应用中需要谨慎处理
            task_type = judge_type(task_context.name)

            if task_type == "代码与练习":
                edit_coder(task)
            elif task_type == "实验与学习":
                test_and_study(task)
            elif task_type == "整理与优化":
                clean_and_update(task)
            elif task_type == "设计":
                design(task)
            elif task_type == "开会与对齐":
                meeting_and_talk(task)
            else:
                print('新的类别')
                meeting_and_talk(task) # 默认处理方式

            task_result = Display.display_dialog("判断", f"任务是否完成: ", buttons='"complete","blockage"', button_cancel=True)
            if task_result == 'complete':
                # 移动到完成池
                pass
            elif task_result == 'blockage':
                # TODO 任务阻塞处理
                # 移动到阻塞池
                pass
            elif task_result == 'no complete':
                # 缩小时间
                # 移动到就绪池
                pass

            else:
                print('ok')

            if task_context.script_code:
                # Execute the script code
                exec(task_context.script_code)
                return f"脚本任务 '{task_context.name}' 执行完毕。"
            else:
                 return f"脚本任务 '{task_context.name}' 没有提供脚本代码。"
        except Exception as e:
            # The state transition on failure would need to be handled by the caller (e.g., TodoState.complete)
            # Or we could return a special error message and let the State decide how to handle it.
            # For simplicity now, just return the error message.
            return f"脚本任务 '{task_context.name}' 执行失败：{e}"
