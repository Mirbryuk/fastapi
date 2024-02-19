
from typing import Union
from fastapi import FastAPI, Response, status
from fastapi.responses import HTMLResponse
from routers import  drivers, trips, users
import uvicorn

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(drivers.router)
app.include_router(trips.router)

@app.get("/", response_class=HTMLResponse)
def root():
    return "<h1>This is the root</h1>"