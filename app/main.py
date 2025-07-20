import logging
from . import models
from .database import engine
from .repository import get_db
from fastapi import FastAPI, Query
from app.models import FlightEvent
from app.services.search_strategies import OneConnectionSearch
from app.services.search_service import FlightSearchService
from app.services.flight_index import FlightIndex

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


#usarlo en los endpoints
logging.basicConfig(filename="app/app.log",  
    level=logging.INFO,  
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    datefmt="%Y-%m-%d %H:%M:%S", 
    filemode='a')
logger = logging.getLogger(__name__)

# Mock data
mock_flights = [
    FlightEvent(flight_number="A1", from_city="NYC", to_city="CHI", departure_time="2025-07-19T08:00:00", arrival_time="2025-07-19T10:00:00"),
    FlightEvent(flight_number="B2", from_city="CHI", to_city="LAX", departure_time="2025-07-19T11:30:00", arrival_time="2025-07-19T13:30:00"),
    FlightEvent(flight_number="C3", from_city="NYC", to_city="LAX", departure_time="2025-07-19T09:00:00", arrival_time="2025-07-19T12:00:00"),
]

@app.on_event("startup")
def startup_event():
    get_db()


@app.get("/journeys/search")
def search_journeys(
    from_city: str = Query(...),
    to_city: str = Query(...),
    date: str = Query(...)
):
    logger.info("GET /journeys/search  %s %s %s", from_city, to_city, date)
    index = FlightIndex(mock_flights, date)
    strategy = OneConnectionSearch(index, from_city, to_city)
    service = FlightSearchService(strategy)
    journeys = service.search()
    return journeys