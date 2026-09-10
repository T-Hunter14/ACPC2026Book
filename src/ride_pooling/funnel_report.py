"""Run the historical simulator funnel and write auditable report artifacts."""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path

from .candidate_engine import HistoricalCandidate, generate_candidates
from .config import SimulatorConfig, load_config
from .loader import HistoricalTrip, load_trips


@dataclass(frozen=True)
class FunnelRow:
    candidate_id: str
    trip_ids: str
    pickup_area: str
    candidate_generated: bool
    feasible: bool
    priced: bool
    extra_minutes: float
    extra_meters: float
    saving_percent: float
    pooled_fare: float
    rejection_reason: str = ""


def run_funnel(trips: list[HistoricalTrip], config: SimulatorConfig | None = None) -> tuple[dict, list[FunnelRow]]:
    settings = config or load_config()
    candidates = generate_candidates(trips, settings)
    by_id = {trip.trip_id: trip for trip in trips}
    rows: list[FunnelRow] = []
    for number, candidate in enumerate(candidates, start=1):
        members = [by_id[trip_id] for trip_id in candidate.trip_ids]
        extra_minutes = max(trip.duration_minutes for trip in members) - min(
            trip.duration_minutes for trip in members
        )
        extra_meters = abs(max(trip.distance for trip in members) - min(trip.distance for trip in members)) * 1609.344
        saving_percent = 100.0 / len(members)
        pooled_fare = sum(trip.fare for trip in members) * (1 - settings.minimum_saving_percent[0] / 100)
        feasible = (
            extra_minutes <= settings.maximum_extra_minutes[1]
            and extra_meters <= settings.maximum_extra_meters
            and saving_percent >= settings.minimum_saving_percent[0]
        )
        priced = feasible and pooled_fare >= sum(trip.fare for trip in members) * (
            1 - settings.driver_incremental_profit_margin_percent[1] / 100
        )
        reason = "" if priced else ("infeasible" if not feasible else "pricing_threshold")
        rows.append(
            FunnelRow(
                candidate_id=f"candidate-{number:04d}",
                trip_ids="|".join(candidate.trip_ids),
                pickup_area=candidate.pickup_area,
                candidate_generated=True,
                feasible=feasible,
                priced=priced,
                extra_minutes=round(extra_minutes, 6),
                extra_meters=round(extra_meters, 6),
                saving_percent=round(saving_percent, 6),
                pooled_fare=round(pooled_fare, 2),
                rejection_reason=reason,
            )
        )
    metrics = {
        "trips_loaded": len(trips),
        "candidates_generated": len(candidates),
        "feasible_candidates": sum(row.feasible for row in rows),
        "priced_candidates": sum(row.priced for row in rows),
    }
    return metrics, rows


def write_report(metrics: dict, rows: list[FunnelRow], output_dir: str | Path) -> tuple[Path, Path]:
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    metrics_path = directory / "funnel_metrics.json"
    rows_path = directory / "funnel_rows.csv"
    metrics_path.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    with rows_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(asdict(rows[0]).keys()) if rows else list(FunnelRow.__dataclass_fields__))
        writer.writeheader()
        writer.writerows(asdict(row) for row in rows)
    return metrics_path, rows_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the historical NYC TLC simulator funnel.")
    parser.add_argument("source", help="Local CSV, ZIP, GZIP, or TLC URL")
    parser.add_argument("--output-dir", default="data/report", help="Directory for JSON and CSV outputs")
    parser.add_argument("--config", type=Path, default=None, help="Optional TOML configuration path")
    args = parser.parse_args()
    config = load_config(args.config) if args.config else load_config()
    metrics, rows = run_funnel(load_trips(args.source), config)
    metrics_path, rows_path = write_report(metrics, rows, args.output_dir)
    print(json.dumps(metrics, sort_keys=True))
    print(f"metrics={metrics_path}")
    print(f"rows={rows_path}")


if __name__ == "__main__":
    main()
