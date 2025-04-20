from fastapi import APIRouter
from typing import List
from app.models.task import Task
from app.services.task_service import task_service


router = APIRouter()


@router.get("/tasks", response_model=List[Task], tags=["tasks"])
def get_tasks():
    return task_service.list_tasks()
