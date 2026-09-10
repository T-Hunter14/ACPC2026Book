"""Load the single source of simulator defaults."""

from dataclasses import dataclass
from pathlib import Path
import tomllib

DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[2] / "config" / "defaults.toml"


@dataclass(frozen=True)
class SimulatorConfig:
    starting_area_size_m: tuple[int, int]
    matching_time_window_minutes: tuple[int, int]
    maximum_wait_before_decision_minutes: tuple[float, float]
    max_passengers: int
    maximum_extra_minutes: tuple[int, int]
    maximum_extra_meters: int
    minimum_saving_percent: tuple[int, int]
    driver_incremental_profit_margin_percent: tuple[int, int]
    driver_offer_wait_seconds: tuple[int, int]
    maximum_offer_attempts: int
    demand_density_requests: tuple[int, int]
    demand_density_window_minutes: int


def load_config(path: Path = DEFAULT_CONFIG_PATH) -> SimulatorConfig:
    """Read and validate the central TOML configuration."""
    with path.open("rb") as config_file:
        raw = tomllib.load(config_file)

    def pair(section: str, minimum: str, maximum: str, cast):
        values = raw[section]
        return cast(values[minimum]), cast(values[maximum])

    config = SimulatorConfig(
        starting_area_size_m=pair("starting_area_size_m", "minimum", "maximum", int),
        matching_time_window_minutes=pair("matching_time_window_minutes", "minimum", "maximum", int),
        maximum_wait_before_decision_minutes=pair(
            "maximum_wait_before_decision_minutes", "minimum", "maximum", float
        ),
        max_passengers=int(raw["pool"]["max_passengers"]),
        maximum_extra_minutes=pair(
            "detour", "maximum_extra_minutes_minimum", "maximum_extra_minutes_maximum", int
        ),
        maximum_extra_meters=int(raw["detour"]["maximum_extra_meters"]),
        minimum_saving_percent=pair(
            "passenger", "minimum_saving_percent_minimum", "minimum_saving_percent_maximum", int
        ),
        driver_incremental_profit_margin_percent=pair(
            "driver",
            "incremental_profit_margin_percent_minimum",
            "incremental_profit_margin_percent_maximum",
            int,
        ),
        driver_offer_wait_seconds=pair("driver", "offer_wait_seconds_minimum", "offer_wait_seconds_maximum", int),
        maximum_offer_attempts=int(raw["driver"]["maximum_offer_attempts"]),
        demand_density_requests=pair("demand", "minimum_requests_minimum", "minimum_requests_maximum", int),
        demand_density_window_minutes=int(raw["demand"]["window_minutes"]),
    )
    _validate(config)
    return config


def _validate(config: SimulatorConfig) -> None:
    for name in (
        "starting_area_size_m",
        "matching_time_window_minutes",
        "maximum_wait_before_decision_minutes",
        "maximum_extra_minutes",
        "minimum_saving_percent",
        "driver_incremental_profit_margin_percent",
        "driver_offer_wait_seconds",
        "demand_density_requests",
    ):
        low, high = getattr(config, name)
        if low <= 0 or high < low:
            raise ValueError(f"{name} must be positive and ordered")
    if config.max_passengers < 2 or config.maximum_offer_attempts < 1:
        raise ValueError("pool capacity and offer attempts must be valid")
    if config.maximum_extra_meters <= 0 or config.demand_density_window_minutes <= 0:
        raise ValueError("distance and demand window must be positive")
