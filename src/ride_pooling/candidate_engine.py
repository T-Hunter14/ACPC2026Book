"""Generate deterministic historical pool candidates from normalized TLC trips."""

from dataclasses import dataclass
from datetime import datetime

from .config import SimulatorConfig, load_config
from .loader import HistoricalTrip


@dataclass(frozen=True)
class HistoricalCandidate:
    trip_ids: tuple[str, ...]
    pickup_area: str
    first_request_time: datetime
    last_request_time: datetime


def generate_candidates(
    trips: list[HistoricalTrip],
    config: SimulatorConfig | None = None,
) -> list[HistoricalCandidate]:
    """Group same-area historical trips within the configured time window.

    Trips are sorted by request time and ID for deterministic output. A
    passenger-count capacity is enforced using the normalized trip counts.
    """
    settings = config or load_config()
    window_minutes = settings.matching_time_window_minutes[1]
    candidates: list[HistoricalCandidate] = []
    by_area: dict[str, list[HistoricalTrip]] = {}
    for trip in trips:
        by_area.setdefault(trip.pickup_area, []).append(trip)

    for area in sorted(by_area):
        ordered = sorted(by_area[area], key=lambda trip: (trip.request_time, trip.trip_id))
        for index, first in enumerate(ordered):
            members = [first]
            passenger_total = first.passenger_count
            for trip in ordered[index + 1 :]:
                elapsed = (trip.request_time - first.request_time).total_seconds() / 60
                if elapsed > window_minutes:
                    break
                if passenger_total + trip.passenger_count > settings.max_passengers:
                    continue
                members.append(trip)
                passenger_total += trip.passenger_count
            if len(members) > 1:
                candidates.append(
                    HistoricalCandidate(
                        trip_ids=tuple(trip.trip_id for trip in members),
                        pickup_area=area,
                        first_request_time=first.request_time,
                        last_request_time=members[-1].request_time,
                    )
                )
    return candidates
