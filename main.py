from fastapi import FastAPI
from group import groupByDate

app = FastAPI()

@app.get("/data")

def get_data():
    result = groupByDate()
    return result