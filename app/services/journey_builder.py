from datetime import datetime,timedelta  
from app.services.journey import Journey

class JourneyBuilder:
    MAX_DURATION = timedelta(hours=24)
    MAX_LAYOVER = timedelta(hours=4)

    @staticmethod
    def build_if_valid(flights):
        if len(flights) > 2:
            return None
        duration = datetime.fromisoformat(flights[-1].arrival_time) - datetime.fromisoformat(flights[0].departure_time)
        if duration > JourneyBuilder.MAX_DURATION:
            return None
        if len(flights) == 2:
            layover = datetime.fromisoformat(flights[1].departure_time) - datetime.fromisoformat(flights[0].arrival_time)
            if not (timedelta(0) <= layover <= JourneyBuilder.MAX_LAYOVER):
                return None
        return Journey(flights)