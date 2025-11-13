import json
import logging
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Iterable, List, Any

logger = logging.getLogger(__name__)

def _to_dict(obj: Any) -> dict:
    if is_dataclass(obj):
        return asdict(obj)
    if isinstance(obj, dict):
        return obj
    raise TypeError(f"Unsupported record type: {type(obj)!r}")

def export_records_to_jsonl(records: Iterable[Any], path: Path) -> None:
    """
    Write parsed records to a JSON Lines file.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8") as f:
        for record in records:
            obj = _to_dict(record)
            f.write(json.dumps(obj, default=str))
            f.write("\n")
            count += 1
    logger.info("Exported %d records to %s", count, path)

def export_summary_to_stdout(command: str, records: List[Any]) -> None:
    """
    Print a lightweight human-readable summary to stdout.
    """
    logger.info("Command '%s' produced %d records", command, len(records))