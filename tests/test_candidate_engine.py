import unittest
from pathlib import Path

from ride_pooling.candidate_engine import generate_candidates
from ride_pooling.config import load_config
from ride_pooling.loader import load_trips


FIXTURE = Path(__file__).parent / "fixtures" / "tlc_yellow_sample.csv"


class CandidateEngineTests(unittest.TestCase):
    def test_generates_same_area_candidates_with_configured_capacity(self):
        candidates = generate_candidates(load_trips(FIXTURE))
        self.assertEqual(
            [(candidate.pickup_area, candidate.trip_ids) for candidate in candidates],
            [("100", ("1", "2")), ("100", ("2", "3"))],
        )

    def test_does_not_cross_pickup_areas_or_configured_window(self):
        config = load_config()
        trips = load_trips(FIXTURE)
        candidates = generate_candidates(trips, config)
        self.assertTrue(all(candidate.pickup_area == "100" for candidate in candidates))
        self.assertTrue(
            all(
                (candidate.last_request_time - candidate.first_request_time).total_seconds() / 60
                <= config.matching_time_window_minutes[1]
                for candidate in candidates
            )
        )
