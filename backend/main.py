from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for the response
class MessageResponse(BaseModel):
    message: str

@app.get("/", response_model=MessageResponse)
def read_root():
    return {"message": "FastAPI is running successfully!"}  # ✅ Always return a dictionary
