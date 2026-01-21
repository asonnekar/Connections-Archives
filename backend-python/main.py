from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from group import groupByDate

app = FastAPI()


origins = [
    "http://localhost:5173",   
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data/{date}")
async def get_data(date: str):
    result = groupByDate(date)
    return result
