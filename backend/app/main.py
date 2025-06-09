from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Teacher app is live!"}
