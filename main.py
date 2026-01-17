from fastapi import FastAPI
from group import groupByDate

app = FastAPI()

@app.get("/data")

def get_data():
    date = '2023-06-12'
    result = groupByDate(date)
    return result