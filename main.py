from typing import Text
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


app = FastAPI()

db = []

class Data(BaseModel):
    id: str
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()




@app.get('/')
async def root():
    return {'message':'CRUD EN FASTAPI'}

@app.get('/data')
async def get_data():
    return db

@app.post('/data')
async def post_data(data: Data):
    db.append(data.dict())
    return "received"
