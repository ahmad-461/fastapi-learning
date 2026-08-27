from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"welcome": "hello ahmad khan"}
@app.get("/about")
def about():
    return {"welcome": "i am student of computer science"}
    
