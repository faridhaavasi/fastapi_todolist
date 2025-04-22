from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from tasks import routs  # import tasks.routs as routs

app = FastAPI(
    title="Simple Todo App Api",
    description="this is a simple blog app with minimal usage of authentication and post managing",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "farid habasi",
        "url": "http://example.com/contact/",
        "email": "faridhavasi777@gmail.com",
    },
    license_info={"name": "MIT"},
    docs_url="/docs",  # default is /docs
)

# Redirect root URL to docs
app.include_router(routs.router)
