"""Deterministic in-memory boundary for Phase 2 real-time matching.

This module deliberately stops at an application/service boundary.  It has no
transport, persistence, routing, dispatch, or negotiation integration.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol

from .candidate_engine import generate_candidates
from .config import SimulatorConfig, load_config
from .loader import HistoricalTrip


@dataclass(frozen=True)
class MatchRequest:
    request_id: str
    request_time: datetime
    pickup_area: str
    dropoff_area: str
    fare: float
    distance: float
    duration_minutes: float
    passenger_count: int = 1


@dataclass(frozen=True)
class MatchResult:
    request_ids: tuple[str, ...]
    pickup_area: str
    pooled_fare: float
    saving_percent: float


class MatchService(Protocol):
    def submit(self, request: MatchRequest) -> None: ...

    def match(self, *, as_of: datetime) -> tuple[MatchResult, ...]: ...


def validate_request(request: MatchRequest, config: SimulatorConfig | None = None) -> None:
    """Reject malformed requests before they enter the service boundary."""
    if not request.request_id.strip():
        raise ValueError("request_id is required")
    if not request.pickup_area.strip() or not request.dropoff_area.strip():
        raise ValueError("pickup_area and dropoff_area are required")
    if request.fare < 0 or request.distance < 0 or request.duration_minutes <= 0:
        raise ValueError("fare and distance must be non-negative; duration must be positive")
    if request.passenger_count < 1:
        raise ValueError("passenger_count must be positive")
    settings = config or load_config()
    if request.passenger_count > settings.max_passengers:
        raise ValueError("passenger_count exceeds configured pool capacity")


class InMemoryMatchService:
    """Small deterministic adapter that matches each request at most once."""

    def __init__(self, config: SimulatorConfig | None = None) -> None:
        self._config = config or load_config()
        self._requests: dict[str, MatchRequest] = {}
        self._matched: set[str] = set()

    def submit(self, request: MatchRequest) -> None:
        validate_request(request, self._config)
        if request.request_id in self._requests:
            raise ValueError(f"duplicate request_id: {request.request_id}")
        self._requests[request.request_id] = request

    def match(self, *, as_of: datetime) -> tuple[MatchResult, ...]:
        pending = [
            request
            for request in self._requests.values()
            if request.request_id not in self._matched and request.request_time <= as_of
        ]
        trips = [_as_historical(request) for request in pending]
        candidates = generate_candidates(trips, self._config)
        by_id = {request.request_id: request for request in pending}
        results: list[MatchResult] = []
        for candidate in candidates:
            if any(request_id in self._matched for request_id in candidate.trip_ids):
                continue
            members = [by_id[request_id] for request_id in candidate.trip_ids]
            total_fare = sum(request.fare for request in members)
            saving_percent = 100.0 / len(members)
            if saving_percent < self._config.minimum_saving_percent[0]:
                continue
            pooled_fare = round(total_fare * (1 - self._config.minimum_saving_percent[0] / 100), 2)
            results.append(
                MatchResult(
                    request_ids=candidate.trip_ids,
                    pickup_area=candidate.pickup_area,
                    pooled_fare=pooled_fare,
                    saving_percent=round(saving_percent, 6),
                )
            )
            self._matched.update(candidate.trip_ids)
        return tuple(results)


def _as_historical(request: MatchRequest) -> HistoricalTrip:
    return HistoricalTrip(
        trip_id=request.request_id,
        request_time=request.request_time,
        pickup_area=request.pickup_area,
        dropoff_area=request.dropoff_area,
        fare=request.fare,
        distance=request.distance,
        duration_minutes=request.duration_minutes,
        passenger_count=request.passenger_count,
        status="pending",
    )
