
from .abstra import TaskState
from .execution_strategy import ScriptTaskExecutionStrategy, PersonTaskExecutionStrategy

# 具体状态类
class TodoState(TaskState):
    def handle(self, task_context):
        # handle for Todo state just returns the initial prompt
        return f"请开始任务：{task_context.name}"

    def complete(self, task_context):
        # print(f"Task '{task_context.name}' from '待办' entering '进行中' state")
        # BEFORE changing state, execute the strategy if it's a ScriptTask
        # This is the trigger point for script execution

        if isinstance(task_context.execution_strategy, ScriptTaskExecutionStrategy) or \
           isinstance(task_context.execution_strategy, PersonTaskExecutionStrategy):
            #  print(f"Task '{task_context.name}' is an executable task type (Script/Person). Executing strategy on starting...")
             # Execute the strategy
             execution_result = task_context.execution_strategy.execute(task_context)
            #  print(f"Strategy Execution Result: {execution_result}") # Print the result of the execution
             # Note: The task's state is set to InProgress regardless of execution success/failure here.
             # You might want to add a FailureState if execution fails significantly.

        # Now change the state to InProgress
        task_context.set_state(InProgressState())
        return f"任务 '{task_context.name}' 状态更新为：进行中"

    def get_status(self):
        return "待办"

class InProgressState(TaskState):
    def handle(self, task_context):
        return f"任务 '{task_context.name}' 正在进行中。请确认是否已完成？"

    def complete(self, task_context):
        # print(f"Task '{task_context.name}' from '进行中' entering '完成' state")
        task_context.set_state(CompletedState())
        return f"任务 '{task_context.name}' 已标记为：完成"

    def get_status(self):
        return "进行中"

class CompletedState(TaskState):
    def handle(self, task_context):
        return f"任务 '{task_context.name}' 已完成。"

    def complete(self, task_context):
        return f"任务 '{task_context.name}' 已处于完成状态，无需重复操作。"

    def get_status(self):
        return "完成"
