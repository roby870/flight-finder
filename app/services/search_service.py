class FlightSearchService:
    def __init__(self, strategy):
        self.strategy = strategy

    def search(self):
        return self.strategy.find_journeys()
