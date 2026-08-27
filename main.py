from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {
        "welcome": "hello ahmad khan",
        "about": "i am student of computer science"
    }
