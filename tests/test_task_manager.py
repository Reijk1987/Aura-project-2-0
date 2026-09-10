from orchestrator.task_manager.manager import TaskManager
from orchestrator.task_manager.models import TaskStatus


def test_task_lifecycle():
    manager = TaskManager()

    task = manager.create_task(
        "task-1",
        "Test AURA task",
    )

    assert task.status == TaskStatus.PENDING

    manager.assign_agent("task-1", "coding")

    assert task.assigned_agent == "coding"

    manager.start_task("task-1")

    assert task.status == TaskStatus.RUNNING

    manager.complete_task("task-1")

    assert task.status == TaskStatus.COMPLETED
