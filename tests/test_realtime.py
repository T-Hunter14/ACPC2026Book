from dataclasses import replace
from datetime import datetime
import unittest

from ride_pooling.realtime import InMemoryMatchService, MatchRequest


class RealtimeMatchingTests(unittest.TestCase):
    def request(self, request_id: str, minutes: int = 0) -> MatchRequest:
        return MatchRequest(
            request_id=request_id,
            request_time=datetime(2026, 1, 1, 12, minutes),
            pickup_area="100",
            dropoff_area="200",
            fare=10.0,
            distance=2.0,
            duration_minutes=10.0,
        )

    def test_matching_is_deterministic_and_idempotent(self):
        service = InMemoryMatchService()
        service.submit(self.request("b", 1))
        service.submit(self.request("a", 0))

        result = service.match(as_of=datetime(2026, 1, 1, 12, 2))
        self.assertEqual(result[0].request_ids, ("a", "b"))
        self.assertEqual(result[0].pooled_fare, 17.0)
        self.assertEqual(service.match(as_of=datetime(2026, 1, 1, 12, 2)), ())

    def test_future_requests_wait_for_as_of(self):
        service = InMemoryMatchService()
        service.submit(self.request("a", 0))
        service.submit(self.request("b", 7))
        self.assertEqual(service.match(as_of=datetime(2026, 1, 1, 12, 6)), ())
        self.assertEqual(
            service.match(as_of=datetime(2026, 1, 1, 12, 7))[0].request_ids,
            ("a", "b"),
        )

    def test_duplicate_and_invalid_requests_are_rejected(self):
        service = InMemoryMatchService()
        service.submit(self.request("a"))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            service.submit(self.request("a"))
        with self.assertRaisesRegex(ValueError, "duration"):
            service.submit(replace(self.request("bad"), duration_minutes=0))
