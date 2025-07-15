# tasks/routes.py
from fastapi import APIRouter

router = APIRouter( 
    prefix="/tasks",
    tags=["Tasks"]
    )

@router.get('/retrieve_tasks')
def retrieve_tasks():
    return []
