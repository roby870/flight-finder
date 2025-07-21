from datetime import timedelta
from app.services.journey import Journey


class JourneyBuilder:
    MAX_DURATION = timedelta(hours=24)
    MAX_LAYOVER = timedelta(hours=4)

    @staticmethod
    def build_if_valid(flights):
        if len(flights) > 2:
            return None
        duration = flights[-1].arrival_time - flights[0].departure_time
        if duration > JourneyBuilder.MAX_DURATION:
            return None
        if len(flights) == 2:
            layover = flights[1].departure_time - flights[0].arrival_time
            if not (timedelta(0) <= layover <= JourneyBuilder.MAX_LAYOVER):
                return None
        return Journey(flights)
