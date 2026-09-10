import unittest
from pathlib import Path

from ride_pooling.config import load_config
from ride_pooling.loader import load_trips

FIXTURE = Path(__file__).parent / "fixtures" / "tlc_yellow_sample.csv"
INVALID_FIXTURE = Path(__file__).parent / "fixtures" / "tlc_invalid_sample.csv"


class LoaderTests(unittest.TestCase):
    def test_loads_tlc_aliases_and_derives_duration(self):
        trips = load_trips(FIXTURE)
        self.assertEqual(len(trips), 4)
        self.assertEqual(trips[0].trip_id, "1")
        self.assertEqual(trips[0].pickup_area, "100")
        self.assertEqual(trips[0].duration_minutes, 15)
        self.assertEqual(trips[1].passenger_count, 2)

    def test_rejects_invalid_trip_instead_of_silently_dropping_it(self):
        with self.assertRaisesRegex(ValueError, "line 2"):
            load_trips(INVALID_FIXTURE)

    def test_defaults_are_loaded_from_central_config(self):
        config = load_config()
        self.assertEqual(config.max_passengers, 3)
        self.assertEqual(config.starting_area_size_m, (300, 800))
        self.assertEqual(config.maximum_offer_attempts, 2)
        self.assertEqual(config.demand_density_requests, (15, 20))
