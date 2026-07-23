import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")
EXPECTED_KEYS = {"total_requests", "unique_ips", "top_path"}


def _load_report() -> dict:
    try:
        report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise AssertionError("/app/report.json was not created") from None
    except json.JSONDecodeError as exc:
        raise AssertionError("/app/report.json is not valid JSON") from exc

    assert isinstance(report, dict), "/app/report.json must contain a JSON object"
    return report


def test_report_format():
    """Success criterion 1: the report is valid JSON with exactly the required keys."""
    report = _load_report()
    assert set(report) == EXPECTED_KEYS


def test_total_requests():
    """Success criterion 2: total_requests is 6."""
    report = _load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Success criterion 3: unique_ips is 3."""
    report = _load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Success criterion 4: top_path is /index.html."""
    report = _load_report()
    assert report["top_path"] == "/index.html"
