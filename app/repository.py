import os
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from . import schemas
from .models import FlightEvent

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_initial_data(db: Session):
    if db.query(FlightEvent).count() == 0:
        db.add(FlightEvent(flight_number="A1", from_city="NYC", to_city="CHI", departure_time="2025-07-19T08:00:00", arrival_time="2025-07-19T10:00:00"))
        db.add(FlightEvent(flight_number="B2", from_city="CHI", to_city="LAX", departure_time="2025-07-19T11:30:00", arrival_time="2025-07-19T13:30:00"))
        db.add(FlightEvent(flight_number="C3", from_city="NYC", to_city="LAX", departure_time="2025-07-19T09:00:00", arrival_time="2025-07-19T12:00:00"))
        db.commit()
        


def get_db():
    db = SessionLocal()
    try:
        create_initial_data(db)
        yield db
    finally:
        db.close()

