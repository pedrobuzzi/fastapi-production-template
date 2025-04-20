from typing import List
from app.models.task import Task


class TaskService:
    def __init__(self):
        self.tasks = [
            Task(id=1, title="Do laundry"),
            Task(id=2, title="Write blog post", completed=True),
        ]

    def list_tasks(self) -> List[Task]:
        return self.tasks


task_service = TaskService()
