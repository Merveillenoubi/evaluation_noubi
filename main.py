from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API FastAPI"}

@app.get("/status")
def get_status():
    return {"status": "ok"}
