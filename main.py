from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"welcome": "hello ahmad khan"}
@app.get(/about)
def hello():
    return{"message":"i am student of computer science}
