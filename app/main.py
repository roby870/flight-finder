import logging
from . import models
from .database import engine
from .repository import get_db
from fastapi import FastAPI, Query
from app import service
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.exception_handlers import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import status, Request

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": exc.errors(), "body": exc.body},
    )


logging.basicConfig(
    filename="app/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filemode="a",
)
logger = logging.getLogger(__name__)


@app.on_event("startup")
def startup_event():
    get_db()


@app.get("/journeys/search")
def search_journeys(
    from_city: str = Query(...),
    to_city: str = Query(...),
    date: str = Query(...),
    db: Session = Depends(get_db),
):
    """
    Search for flight journeys between two cities on a given date.

    Parameters:
        from_city (str): Departure city (IATA code or name).
        to_city (str): Arrival city (IATA code or name).
        date (str): Departure date in YYYY-MM-DD format.
        db (Session): Database session (injected).

    Returns:
        List[dict]: List of journeys, each with:
            - connections: number of connections (0 for direct flight)
            - path: list of flight segments, each with keys:
                - flight_number
                - from
                - to
                - departure_time (YYYY-MM-DD HH:MM)
                - arrival_time (YYYY-MM-DD HH:MM)

    Example response:
    [
      {
        "connections": 0,
        "path": [
          {
            "flight_number": "XX1234",
            "from": "BUE",
            "to": "MAD",
            "departure_time": "2024-09-12 12:00",
            "arrival_time": "2024-09-13 00:00"
          }
        ]
      }
    ]
    """

    logger.info("GET /journeys/search  %s %s %s", from_city, to_city, date)
    journeys = service.get_flights(db, date, from_city, to_city)
    return journeys
