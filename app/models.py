from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP

class FlightEvent(Base):
    __tablename__ = "flight_events"

    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String, nullable=False)
    from_city = Column(String, nullable=False)
    to_city = Column(String, nullable=False)
    departure_time = Column(TIMESTAMP(timezone=True), nullable=False)
    arrival_time = Column(TIMESTAMP(timezone=True), nullable=False)
    