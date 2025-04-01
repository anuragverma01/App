from fastapi import FastAPI, Query
from pymongo import MongoClient

app = FastAPI()

# 🔥 MongoDB Connection
client = MongoClient("mongodb+srv://veggie:hc9ohMc6GXZE8jfv@cluster0.ffxx0rq.mongodb.net/veggieDB?retryWrites=true&w=majority")
db = client["fire_risk_db"]
risk_collection = db["fire_risk_predictions"]
live_fire = db["weather_data"]

# 📌 Fire Risk API with limit=all Support
@app.get("/fire-risk")
async def get_fire_risk_data(page: int = Query(1, alias="page"), limit: str = Query("50", alias="limit")):
    """
    Fetch fire risk data with pagination OR fetch all data if limit=all.
    """
    if limit == "all":
        fire_risk_data = list(risk_collection.find({}, {"_id": 0}))
        return {"data": fire_risk_data}

    limit = int(limit)  # Convert limit to integer
    skip = (page - 1) * limit  # Calculate offset
    fire_risk_data = list(risk_collection.find({}, {"_id": 0}).skip(skip).limit(limit))
    return {"data": fire_risk_data, "page": page, "limit": limit}


# 📌 Live Fire API with limit=all Support
@app.get("/live-fire")
async def get_live_fire_data(page: int = Query(1, alias="page"), limit: str = Query("50", alias="limit")):
    """
    Fetch live fire data with pagination OR fetch all data if limit=all.
    """
    if limit == "all":
        live_fire_data = list(live_fire.find({}, {"_id": 0}))
        return {"data": live_fire_data}

    limit = int(limit)  # Convert limit to integer
    skip = (page - 1) * limit  # Calculate offset
    live_fire_data = list(live_fire.find({}, {"_id": 0}).skip(skip).limit(limit))
    return {"data": live_fire_data, "page": page, "limit": limit}
