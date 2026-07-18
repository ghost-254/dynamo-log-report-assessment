import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.is_file(), "missing /app/report.json"
    try:
        return json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError("/app/report.json is not valid JSON") from exc


def test_report_schema():
    """Criterion 1: the report is a JSON object with exactly the required typed fields."""
    report = load_report()
    assert type(report) is dict
    assert set(report) == {"total_requests", "unique_ips", "top_path"}
    assert type(report["total_requests"]) is int
    assert type(report["unique_ips"]) is int
    assert type(report["top_path"]) is str


def test_report_values():
    """Criterion 2: the report accurately summarizes every record in the supplied log."""
    report = load_report()
    assert report["total_requests"] == 6
    assert report["unique_ips"] == 3
    assert report["top_path"] == "/index.html"
