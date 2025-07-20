from collections import defaultdict
from datetime import datetime
from zoneinfo import ZoneInfo

class FlightIndex:
    def __init__(self, flights, date):
        self.flights = [f for f in flights if datetime.fromisoformat(f.departure_time).astimezone(ZoneInfo("UTC")).strftime("%Y-%m-%d") == date]
        self.by_origin = defaultdict(list)
        for f in self.flights:
            self.by_origin[f.from_city].append(f)

    def get_from(self, city):
        return self.by_origin.get(city, [])