from orchestrator.task_manager.models import Task, TaskStatus


class TaskManager:

    def __init__(self) -> None:
        self.tasks: dict[str, Task] = {}

    def create_task(self, task_id: str, description: str) -> Task:
        task = Task(
            id=task_id,
            description=description,
        )
        self.tasks[task_id] = task
        return task

    def assign_agent(self, task_id: str, agent: str) -> Task:
        task = self.tasks[task_id]
        task.assigned_agent = agent
        return task

    def start_task(self, task_id: str) -> Task:
        task = self.tasks[task_id]
        task.status = TaskStatus.RUNNING
        return task

    def complete_task(self, task_id: str) -> Task:
        task = self.tasks[task_id]
        task.status = TaskStatus.COMPLETED
        return task

    def fail_task(self, task_id: str) -> Task:
        task = self.tasks[task_id]
        task.status = TaskStatus.FAILED
        return task

    def get_task(self, task_id: str) -> Task | None:
        return self.tasks.get(task_id)
