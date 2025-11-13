import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from parsers.salaries_parser import parse_salaries  # noqa: E402

def _load_raw() -> list[dict]:
    path = ROOT / "data" / "sample_output.json"
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def test_parse_salaries_basic() -> None:
    raw = _load_raw()
    salary_items = [r for r in raw if r.get("recordType") == "salary"]
    records = parse_salaries(salary_items)

    assert len(records) == 1
    record = records[0]
    assert record.job_title == "Software Engineer"
    assert record.currency_code == "USD"
    assert record.base_pay_p50 == 110000
    assert record.total_pay_p90 == 180000