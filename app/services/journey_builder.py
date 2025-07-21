from abc import ABC, abstractmethod
from datetime import timedelta
from app.services.journey import Journey


class BaseJourneyBuilder(ABC):
    def __init__(self):
        self._flights = []

    def add_flight(self, flight: "FlightEvent") -> "BaseJourneyBuilder":
        self._flights.append(flight)
        return self

    @abstractmethod
    def is_valid_number_of_flights(self) -> bool:
        pass

    @abstractmethod
    def is_valid_duration(self) -> bool:
        pass

    @abstractmethod
    def is_valid_layover(self) -> bool:
        pass

    @abstractmethod
    def build(self) -> Journey | None:
        pass


class StandardJourneyBuilder(BaseJourneyBuilder):
    MAX_DURATION = timedelta(hours=24)
    MAX_LAYOVER = timedelta(hours=4)
    MAX_FLIGHTS = 2

    def is_valid_number_of_flights(self) -> bool:
        return len(self._flights) <= self.MAX_FLIGHTS

    def is_valid_duration(self) -> bool:
        if not self._flights:
            return False
        duration = self._flights[-1].arrival_time - self._flights[0].departure_time
        return duration <= self.MAX_DURATION

    def is_valid_layover(self) -> bool:
        if len(self._flights) != 2:
            return True
        layover = self._flights[1].departure_time - self._flights[0].arrival_time
        return timedelta(0) <= layover <= self.MAX_LAYOVER

    def build(self) -> Journey | None:
        if not self.is_valid_number_of_flights():
            return None
        if not self.is_valid_duration():
            return None
        if not self.is_valid_layover():
            return None
        return Journey(self._flights)
