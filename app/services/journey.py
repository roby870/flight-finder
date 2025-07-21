from datetime import timedelta
from app.models import FlightEvent


class Journey:
    def __init__(self, flights: list[FlightEvent]):
        self.flights = flights

    def total_duration(self) -> timedelta:
        return self.flights[-1].arrival_time - self.flights[0].departure_time

    def connections(self) -> int:
        return len(self.flights) - 1
