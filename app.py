from fastapi import FastAPI,Query
from pymongo import MongoClient

app = FastAPI()

# MongoDB Connection
client = MongoClient("mongodb+srv://veggie:hc9ohMc6GXZE8jfv@cluster0.ffxx0rq.mongodb.net/veggieDB?retryWrites=true&w=majority")
db = client["fire_risk_db"]
risk_collection = db["fire_risk_predictions"]
live_fire = db["weather_data"]

@app.get("/fire-risk")
async def get_fire_risk_data(page: int = Query(1, alias="page"), limit: int = Query(50, alias="limit")):
    """Fetch all fire risk data from MongoDB."""
    skip = (page - 1) * limit  # Calculate offset
    fire_risk_data = list(risk_collection.find({}, {"_id": 0}).skip(skip).limit(limit))  # Exclude _id field
    return {"data":fire_risk_data , "page": page, "limit": limit}


@app.get("/live-fire")
async def get_fire_risk_data(page: int = Query(1, alias="page"), limit: int = Query(50, alias="limit")):
    """
    Fetch live fire data from MongoDB with pagination.
    - `page`: Page number (default: 1)
    - `limit`: Number of records per page (default: 50)
    """
    skip = (page - 1) * limit  # Calculate offset

    live_fire_data = list(live_fire.find({}, {"_id": 0}).skip(skip).limit(limit))  # Pagination applied
    return {"data": live_fire_data, "page": page, "limit": limit}
