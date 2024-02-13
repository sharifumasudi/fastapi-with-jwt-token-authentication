from fastapi import FastAPI
import models
from database import engine
from routers import blogs, login, users

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.get('/', tags=["API's"])
async def index():
    return "Welcome back!"
app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(login.router)