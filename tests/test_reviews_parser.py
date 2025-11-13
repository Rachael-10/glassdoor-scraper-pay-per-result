import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from parsers.reviews_parser import parse_reviews  # noqa: E402

def _load_raw() -> list[dict]:
    path = ROOT / "data" / "sample_output.json"
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def test_parse_reviews_basic() -> None:
    raw = _load_raw()
    review_items = [r for r in raw if r.get("recordType") == "review"]
    records = parse_reviews(review_items)

    assert len(records) == 1
    record = records[0]
    assert record.summary == "Great culture very rewarding"
    assert record.rating_overall == 5
    assert record.employer_short_name == "Kids on the Move"