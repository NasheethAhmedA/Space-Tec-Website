from AI_ChatBot.AI_Gen import Reply, Client
from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()
my_client = Client()

DATA_FILE = "markers.json"

class AI_Reply(BaseModel):
    reply: str

class Marker(BaseModel):
    lat: float
    lng: float

def read_data() -> list[Marker]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def write_data(data: Marker) -> None:
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

@app.get("/")
def read_root():
    return {"Hello": "Hackunia"}

@app.get("/markers", response_model=list[Marker])
def get_markers():
    return read_data()

@app.post("/markers", response_model=Marker)
def add_marker(marker: Marker):
    data = read_data()
    if marker.dict() not in data:
        data.append(marker.dict())
        write_data(data)
    else:
        # Logging the error in the console
        print("Marker already exists")
    return marker

@app.get("/chatbot/{message}", response_model=AI_Reply)
async def root(message: str):
    """
    This endpoint is used to get the response from the chatbot.
    """
    return {"reply": Reply(my_client, message)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
