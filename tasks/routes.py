# tasks/routes.py
from fastapi import APIRouter

router = APIRouter( 
    prefix="/tasks",
    tags=["Tasks"]
    )

@router.get('/retrieve_tasks')
async def retrieve_tasks():
    return []



@router.post('/create_task')
async def create_task():
    return {}

@router.put('/update_task/{id}')
async def update_task(id: int):
    return {}

@router.patch('/update_task/{id}')
async def update_task(id: int):
    return {}

@router.delete('/delete_task/{id}')
async def delete_task(id: int):
    return {}