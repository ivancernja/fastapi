from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, Spaces!", "message": "Welcome to FastAPI!"}