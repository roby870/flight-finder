import logging
from . import models
from .database import engine
from .repository import get_db
from fastapi import FastAPI, Query
from app import service
from sqlalchemy.orm import Session
from fastapi import Depends

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


logging.basicConfig(filename="app/app.log",  
    level=logging.INFO,  
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    datefmt="%Y-%m-%d %H:%M:%S", 
    filemode='a')
logger = logging.getLogger(__name__)


@app.on_event("startup")
def startup_event():
    get_db()


@app.get("/journeys/search")
def search_journeys(
    from_city: str = Query(...),
    to_city: str = Query(...),
    date: str = Query(...),
    db: Session = Depends(get_db)
):
    logger.info("GET /journeys/search  %s %s %s", from_city, to_city, date)
    journeys = service.get_flights(db, date, from_city, to_city)
    return journeys