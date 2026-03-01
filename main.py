from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()



reviews = [
    {
        "id": 1,
        "user": "Ashesh",
        "comment": "FastAPI is extremely fast to develop with and has excellent performance out of the box.",
        "rating": 5
    },
    {
        "id": 2,
        "user": "Developer",
        "comment": "Automatic Swagger documentation makes FastAPI very developer-friendly and easy to test.",
        "rating": 5
    },
    {
        "id": 3,
        "user": "Backend Engineer",
        "comment": "FastAPI's type hints and async support make APIs clean, readable, and scalable.",
        "rating": 4
    }
]


@app.get("/")
def home():
    return {"message": "Hello World"}


@app.get("/api/reviews")
def get_reviews():
    return reviews


@app.get("/notification", response_class=HTMLResponse)
def get_notificaiton():
    return "<h1>Notification</h1>"