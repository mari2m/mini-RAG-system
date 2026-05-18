#uvicorn main:app --reload --host 0.0.0.0 --port 5000
#http://127.0.0.1:8000/docs or use postman

from fastapi import FastAPI
app=FastAPI()

@app.get("/welcome")
def welcome():
    return{
    "massage":"hi"
    }