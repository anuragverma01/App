from fastapi import FastAPI
from pymongo import MongoClient
import os

app = FastAPI()

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI")
db = MONGO_URI["fire_risk_db"]
risk_collection = db["fire_risk_predictions"]
live_fire = db["weather_data"]

@app.get("/fire-risk")
async def get_fire_risk_data():
    """Fetch all fire risk data from MongoDB."""
    
    fire_risk_data = list(risk_collection.find({}, {"_id": 0}))  # Exclude _id field
    return fire_risk_data


@app.get("/live-fire")
async def get_fire_risk_data():
    """Fetch all live fire data from MongoDB."""
    
    live_fire_data = list(live_fire.find({}, {"_id": 0}))  # Exclude _id field
    return live_fire_data

