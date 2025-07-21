from app.services.journey_builder import StandardJourneyBuilder
from app.services.flight_index import FlightIndex


class JourneySearchBase:
    def __init__(self, index: FlightIndex, from_city: str, to_city: str):
        self.index = index
        self.from_city = from_city
        self.to_city = to_city
        self.journeys = []

    def find_journeys(self):
        for first in self.index.get_from(self.from_city):
            if self.should_add_direct(first):
                j = StandardJourneyBuilder().add_flight(first).build()
                if j:
                    self.journeys.append(j)

            if self.should_add_one_connection():
                for second in self.index.get_from(first.to_city):
                    layover = (
                        second.departure_time - first.arrival_time
                    ).total_seconds()
                    if second.to_city == self.to_city and 0 <= layover <= 4 * 3600:
                        j = StandardJourneyBuilder().add_flight(first).add_flight(second).build()
                        if j:
                            self.journeys.append(j)

        return self.journeys

    def should_add_direct(self, first: "FlightEvent") -> bool:
        return False

    def should_add_one_connection(self) -> bool:
        return False


class DirectOnlySearch(JourneySearchBase):
    def should_add_direct(self, first):
        return first.to_city == self.to_city


class OneConnectionSearch(JourneySearchBase):
    def should_add_direct(self, first):
        return first.to_city == self.to_city

    def should_add_one_connection(self):
        return True
