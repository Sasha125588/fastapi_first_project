from fastapi import APIRouter, Depends
from typing import Annotated, List

from schemas import STaskAdd, STask, STaskId
from repository import TaskRepository

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("")
async def get_tasks() -> List[STask]:
    tasks = await TaskRepository.get_all()
    return {"tasks": tasks}


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add(task)
    return {"task_id": task_id}
