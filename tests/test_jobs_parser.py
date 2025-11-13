import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from parsers.jobs_parser import parse_jobs  # noqa: E402

def _load_raw() -> list[dict]:
    path = ROOT / "data" / "sample_output.json"
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def test_parse_jobs_basic() -> None:
    raw = _load_raw()
    job_items = [r for r in raw if r.get("recordType") == "job"]
    records = parse_jobs(job_items)

    assert len(records) == 1
    record = records[0]
    assert record.job_title_text == "Data Analyst"
    assert record.location_name == "Salt Lake City, UT"
    assert record.pay_currency == "USD"
    assert record.pay_p10 == 60000
    assert record.pay_p90 == 95000