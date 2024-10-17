from fastapi import FastAPI
import sqlalchemy

app = FastAPI(tags=['Tasma Main API'])

@app.get("/")
async def root():
    return {"message": "Hello from Tasma!"}