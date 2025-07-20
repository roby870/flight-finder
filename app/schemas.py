from pydantic import BaseModel
from datetime import datetime

class FlightEventBase(BaseModel):
    flight_number: str
    from_city: str
    to_city: str
    departure_time: datetime
    arrival_time: datetime

class FlightEventCreate(FlightEventBase):
    pass

class FlightEventRead(FlightEventBase):
    id: int

    class Config:
        orm_mode = True