from fastapi import FastAPI
from tasks.routes import router as tasks_router

tags_metadata = [
    {
        "name": "Tasks",
        "description": "Operations related to task management.",
    }
]

app = FastAPI(openapi_tags=tags_metadata)

# include the router
app.include_router(tasks_router)
