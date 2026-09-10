import json
import unittest

from ride_pooling.funnel_report import run_funnel, write_report
from ride_pooling.loader import load_trips


class FunnelReportTests(unittest.TestCase):
    def test_fixture_funnel_is_deterministic(self):
        trips = load_trips("tests/fixtures/tlc_yellow_sample.csv")
        metrics, rows = run_funnel(trips)
        self.assertEqual(
            metrics,
            {
                "trips_loaded": 4,
                "candidates_generated": 2,
                "feasible_candidates": 0,
                "priced_candidates": 0,
            },
        )
        self.assertEqual([row.trip_ids for row in rows], ["1|2", "2|3"])
        self.assertTrue(all(row.priced is False for row in rows))
        metrics_path, rows_path = write_report(metrics, rows, "data/test-report")
        self.assertEqual(json.loads(metrics_path.read_text()), metrics)
        self.assertTrue(
            rows_path.read_text().splitlines()[1].startswith("candidate-0001,1|2,100,True,False,False")
        )
