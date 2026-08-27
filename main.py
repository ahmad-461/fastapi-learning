from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"welcome": "hello ahmad khan"}
@app.get("/")
def hello():
    return {"welcome": "i am student of computer science"}
    
