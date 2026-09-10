# Ride Pooling Simulator

This repository contains the deterministic historical simulator and the
Phase 2 in-memory matching boundary. It is intentionally offline: the tests
and smoke command use the checked-in CSV fixture and do not require network
access.

## Setup

Use Python 3.11 or newer. From the repository root, install the project in
editable mode:

```powershell
python -m pip install -e .
```

No runtime dependency downloads are required after the editable install.

## Test commands

Run the full test suite with the Python standard library test runner:

```powershell
python -m unittest discover -s tests -v
```

Run the offline simulator smoke path:

```powershell
python -m ride_pooling.funnel_report tests/fixtures/tlc_yellow_sample.csv --output-dir data/smoke-report
```

The command writes `data/smoke-report/funnel_metrics.json` and
`data/smoke-report/funnel_rows.csv`.

The single source of simulator defaults is `config/defaults.toml`; the
architecture boundary and excluded production concerns are documented in
`docs/architecture.md`.
