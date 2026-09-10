"""Normalize public NYC TLC trip records into the simulator trip contract."""

from dataclasses import dataclass
from datetime import datetime
import csv
import gzip
from io import TextIOWrapper
from pathlib import Path
import urllib.request
import zipfile


@dataclass(frozen=True)
class HistoricalTrip:
    trip_id: str
    request_time: datetime
    pickup_area: str
    dropoff_area: str
    fare: float
    distance: float
    duration_minutes: float
    passenger_count: int
    status: str = "completed"


_ALIASES = {
    "trip_id": ("trip_id", "VendorID"),
    "request_time": ("request_time", "tpep_pickup_datetime", "lpep_pickup_datetime"),
    "dropoff_time": ("dropoff_time", "tpep_dropoff_datetime", "lpep_dropoff_datetime"),
    "pickup_area": ("pickup_area", "PULocationID", "pickup_zone"),
    "dropoff_area": ("dropoff_area", "DOLocationID", "dropoff_zone"),
    "fare": ("fare", "total_amount"),
    "distance": ("distance", "trip_distance"),
    "passenger_count": ("passenger_count",),
    "status": ("status",),
}


def load_trips(source: str | Path, *, timeout_seconds: int = 30) -> list[HistoricalTrip]:
    """Load a local or HTTP(S) CSV, ZIP, or GZIP TLC export."""
    source_text = str(source)
    if source_text.startswith(("http://", "https://")):
        request = urllib.request.Request(source_text, headers={"User-Agent": "ride-pooling-simulator"})
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            return _load_bytes(response.read(), source_text)

    path = Path(source)
    if not path.is_file():
        raise FileNotFoundError(path)
    if path.suffix.lower() == ".zip":
        with zipfile.ZipFile(path) as archive:
            names = [name for name in archive.namelist() if name.lower().endswith(".csv")]
            if len(names) != 1:
                raise ValueError("ZIP source must contain exactly one CSV")
            with archive.open(names[0]) as stream:
                return _parse_csv(TextIOWrapper(stream, encoding="utf-8-sig", newline=""))
    if path.suffix.lower() == ".gz":
        with gzip.open(path, "rt", encoding="utf-8-sig", newline="") as stream:
            return _parse_csv(stream)
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        return _parse_csv(stream)


def _load_bytes(data: bytes, name: str) -> list[HistoricalTrip]:
    from io import BytesIO, StringIO

    lower_name = name.lower()
    if lower_name.endswith(".zip"):
        with zipfile.ZipFile(BytesIO(data)) as archive:
            names = [item for item in archive.namelist() if item.lower().endswith(".csv")]
            if len(names) != 1:
                raise ValueError("ZIP source must contain exactly one CSV")
            with archive.open(names[0]) as stream:
                return _parse_csv(TextIOWrapper(stream, encoding="utf-8-sig", newline=""))
    if lower_name.endswith(".gz"):
        with gzip.GzipFile(fileobj=BytesIO(data), mode="rb") as stream:
            return _parse_csv(TextIOWrapper(stream, encoding="utf-8-sig", newline=""))
    return _parse_csv(StringIO(data.decode("utf-8-sig", errors="strict"), newline=""))


def _parse_csv(stream) -> list[HistoricalTrip]:
    reader = csv.DictReader(stream)
    if not reader.fieldnames:
        raise ValueError("CSV source has no header")
    fields = {name for name in reader.fieldnames if name}
    resolved = {key: _find_field(fields, aliases) for key, aliases in _ALIASES.items()}
    required = ("trip_id", "request_time", "dropoff_time", "pickup_area", "dropoff_area", "fare", "distance")
    missing = [key for key in required if resolved[key] is None]
    if missing:
        raise ValueError(f"CSV is missing required fields: {', '.join(missing)}")

    trips = []
    for line_number, row in enumerate(reader, start=2):
        try:
            pickup = _required_text(row, resolved["pickup_area"], "pickup area")
            dropoff = _required_text(row, resolved["dropoff_area"], "dropoff area")
            request_time = _parse_datetime(_required_text(row, resolved["request_time"], "request time"))
            dropoff_time = _parse_datetime(_required_text(row, resolved["dropoff_time"], "dropoff time"))
            duration = (dropoff_time - request_time).total_seconds() / 60
            fare = float(_required_text(row, resolved["fare"], "fare"))
            distance = float(_required_text(row, resolved["distance"], "distance"))
            passenger_count = _positive_int(
                row.get(resolved["passenger_count"], "1") if resolved["passenger_count"] else "1"
            )
            if duration <= 0 or fare < 0 or distance < 0:
                raise ValueError("duration must be positive and fare/distance non-negative")
            trips.append(
                HistoricalTrip(
                    trip_id=_required_text(row, resolved["trip_id"], "trip ID"),
                    request_time=request_time,
                    pickup_area=pickup,
                    dropoff_area=dropoff,
                    fare=fare,
                    distance=distance,
                    duration_minutes=duration,
                    passenger_count=passenger_count,
                    status=(row.get(resolved["status"], "completed") or "completed").strip(),
                )
            )
        except (TypeError, ValueError) as error:
            raise ValueError(f"invalid trip at CSV line {line_number}: {error}") from error
    return trips


def _find_field(fields: set[str], aliases: tuple[str, ...]) -> str | None:
    return next((alias for alias in aliases if alias in fields), None)


def _required_text(row: dict, field: str | None, label: str) -> str:
    value = row.get(field, "").strip() if field else ""
    if not value:
        raise ValueError(f"{label} is required")
    return value


def _parse_datetime(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _positive_int(value: str) -> int:
    number = int(float(value))
    if number < 1:
        raise ValueError("passenger count must be positive")
    return number
