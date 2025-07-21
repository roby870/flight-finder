from app.services.search_strategies import OneConnectionSearch
from app.services.search_service import FlightSearchService
from app.services.flight_index import FlightIndex
from . import repository
from sqlalchemy.orm import Session

from .serializer import serialize_journey


def get_flights(db: Session, date: str, from_city: str, to_city: str):
    flights = repository.get_flights(db, date)
    index = FlightIndex(flights, date)
    strategy = OneConnectionSearch(index, from_city, to_city)
    service = FlightSearchService(strategy)
    journeys = service.search()
    return [serialize_journey(j) for j in journeys]
