from fastapi import FastAPI
from blog import router as blog_router
from auth.routes import router as auth_router

app = FastAPI()

app.include_router(
    auth_router,
)

app.include_router(
    blog_router,
    tags=['blog'],
    prefix='/blog'
)
