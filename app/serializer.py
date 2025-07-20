def serialize_journey(journey):
    return {
        "connections": journey.connections(),
        "path": [
            {
                "flight_number": f.flight_number,
                "from": f.from_city,
                "to": f.to_city,
                "departure_time": f.departure_time.strftime("%Y-%m-%d %H:%M"),
                "arrival_time": f.arrival_time.strftime("%Y-%m-%d %H:%M"),
            }
            for f in journey.flights
        ],
    }