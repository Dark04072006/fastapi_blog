import uvicorn
from fastapi import FastAPI
from app.blog.routes import router
from app.core.settings import config
from app.core.database import database


app: FastAPI = FastAPI()

app.include_router(router, prefix='/api/posts', tags=['posts'])

@app.on_event('startup')
async def on_startup():
    await database.connect()


@app.on_event('shutdown')
async def on_shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', host=config.application.host,
                port=config.application.port, reload=True)
