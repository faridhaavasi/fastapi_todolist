from fastapi import FastAPI, Depends
from tasks.routes import router as tasks_router
from users.routes import router as user_router
from users.models import UserModel as User
tags_metadata = [
    {
        "name": "Tasks",
        "description": "Operations related to task management.",
    }
]

app = FastAPI(openapi_tags=tags_metadata)
from auth.bisic_auth import get_authenticated_user


@app.post('publice')
async def publice():
    return {}

@app.post('private')
async def private(current_user: User = Depends(get_authenticated_user)):
    return {}



# include the router
app.include_router(tasks_router)
app.include_router(user_router)
