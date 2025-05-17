from abc import ABC, abstractmethod


# 策略接口
class TaskExecutionStrategy(ABC):
    @abstractmethod
    def execute(self, task_context):
        """执行任务的特定逻辑"""
        pass

# 具体策略：提示任务执行策略
class PromptTaskExecutionStrategy(TaskExecutionStrategy):
    def execute(self, task_context):
        return task_context._state.handle(task_context)

# 具体策略：脚本任务执行策略
class ScriptTaskExecutionStrategy(TaskExecutionStrategy):
    def execute(self, task_context):
        print(f"正在执行脚本任务 '{task_context.name}'...")
        try:
            # 注意：安全问题！这里只是示例
            exec(task_context.script_code)
            return f"脚本任务 '{task_context.name}' 执行完毕。"
        except Exception as e:
            return f"脚本任务 '{task_context.name}' 执行失败：{e}"


##################


# 任务状态接口 (与之前相同) # 状态模式
class TaskState(ABC):
    @abstractmethod
    def handle(self, task_context):
        """处理当前状态下的任务逻辑"""
        pass

    @abstractmethod
    def complete(self, task_context):
        """尝试完成任务"""
        pass

    @abstractmethod
    def get_status(self):
        """获取当前状态描述"""
        pass

# 具体状态类 (与之前相同)
class TodoState(TaskState):
    def handle(self, task_context):
        return f"请开始任务：{task_context.name}"

    def complete(self, task_context):
        print(f"任务 '{task_context.name}' 从 '待办' 进入 '进行中' 状态")
        task_context.set_state(InProgressState())
        return f"任务 '{task_context.name}' 状态更新为：进行中"

    def get_status(self):
        return "待办"

class InProgressState(TaskState):
    def handle(self, task_context):
        return f"任务 '{task_context.name}' 正在进行中。请确认是否已完成？"

    def complete(self, task_context):
        print(f"任务 '{task_context.name}' 从 '进行中' 进入 '完成' 状态")
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

# 任务类 (包含任务名称和状态上下文)
class Task:
    def __init__(self, name: str, execution_strategy: TaskExecutionStrategy,script_code: str = None):
        self.name = name
        self._state = TodoState() # 每个任务实例都有自己的独立状态上下文
        self.execution_strategy = execution_strategy #

    def set_state(self, state: TaskState):
        """设置任务的当前状态"""
        self._state = state

    def request(self):
        """处理任务（查询任务时的逻辑）"""
        print(2222222222)
        return self.execution_strategy.execute(self)
        # return self._state.handle(self)

    def complete_task(self):
        """尝试完成任务（用户确认完成时的逻辑）"""
        return self._state.complete(self)

    def get_status(self):
        """获取当前任务状态描述"""
        return self._state.get_status()

# 任务管理器类 (使用字典管理任务)
class TaskManager:
    def __init__(self):
        self._tasks = {} # 使用字典存储任务，任务名称作为键

    def add_task(self, task_name: str,task_type = 'prompt',script_code: str = None):
        """动态添加任务"""
        if task_name in self._tasks:
            return f"任务 '{task_name}' 已存在。"
        
        if task_type == 'prompt':
            strategy = PromptTaskExecutionStrategy()
        elif task_type == 'script':
            strategy = ScriptTaskExecutionStrategy()
        else:
            strategy = PromptTaskExecutionStrategy()

        # new_task = Task(name=task_name)

        if task_type == 'script':
            new_task = Task(name=task_name, execution_strategy=strategy, script_code=script_code)
        else:
            new_task = Task(name=task_name, execution_strategy=strategy)

        self._tasks[task_name] = new_task
        return f"任务 '{task_name}' 已添加。"

    def get_task(self, task_name: str) -> Task | None:
        """获取指定名称的任务"""
        return self._tasks.get(task_name)

    def check_tasks(self):
        """检查所有未完成的任务并返回提示"""
        prompts = []
        for task_name, task in self._tasks.items():
            # 只检查非完成状态的任务
            if not isinstance(task._state, CompletedState):
                 prompts.append(task.request())
        return prompts

    def complete_task(self, task_name: str):
        """完成指定名称的任务"""
        task = self.get_task(task_name)
        if task:
            return task.complete_task()
        else:
            return f"任务 '{task_name}' 不存在。"

    def get_task_status(self, task_name: str):
        """获取指定任务的状态"""
        task = self.get_task(task_name)
        if task:
            return f"任务 '{task_name}' 的状态是：{task.get_status()}"
        else:
            return f"任务 '{task_name}' 不存在。"

if __name__ == "__main__":
    # 模拟使用
    task_manager = TaskManager()

    # 动态添加任务
    print(task_manager.add_task("检查和收集咨询"))
    print(task_manager.add_task("编写日报"))
    print(task_manager.add_task("学习新知识点"))

    print("\n--- 第一次检查任务 ---")
    for prompt in task_manager.check_tasks():
        print(prompt)

    print("\n--- 完成 '检查和收集咨询' 任务 (第一次完成) ---")
    print(task_manager.complete_task("检查和收集咨询"))
    print(task_manager.get_task_status("检查和收集咨询"))

    print("\n--- 第二次检查任务 ---")
    for prompt in task_manager.check_tasks():
        print(prompt)

    print("\n--- 完成 '检查和收集咨询' 任务 (第二次完成) ---")
    print(task_manager.complete_task("检查和收集咨询"))
    print(task_manager.get_task_status("检查和收集咨询"))

    print("\n--- 完成 '编写日报' 任务 (第一次完成) ---")
    print(task_manager.complete_task("编写日报"))
    print(task_manager.get_task_status("编写日报"))

    print("\n--- 第三次检查任务 ---")
    for prompt in task_manager.check_tasks():
        print(prompt)

    print("\n--- 完成 '编写日报' 任务 (第二次完成) ---")
    print(task_manager.complete_task("编写日报"))
    print(task_manager.get_task_status("编写日报"))

    print("\n--- 完成 '学习新知识点' 任务 ---")
    print(task_manager.complete_task("学习新知识点"))
    print(task_manager.get_task_status("学习新知识点"))

    print("\n--- 第四次检查任务 ---")
    for prompt in task_manager.check_tasks():
        print(prompt)