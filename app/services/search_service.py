from app.services.journey import Journey
from app.services.search_strategies import JourneySearchBase

class FlightSearchService:
    def __init__(self, strategy: JourneySearchBase):
        self.strategy = strategy

    def search(self) -> list[Journey]:
        return self.strategy.find_journeys()
