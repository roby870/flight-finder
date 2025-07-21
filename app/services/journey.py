class Journey:
    def __init__(self, flights):
        self.flights = flights

    def total_duration(self):
        return self.flights[-1].arrival_time - self.flights[0].departure_time

    def connections(self):
        return len(self.flights) - 1
