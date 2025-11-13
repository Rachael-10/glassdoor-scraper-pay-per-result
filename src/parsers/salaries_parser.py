from typing import Any, Dict, List

from storage.schemas import SalaryRecord

def _extract_percentile(statistics: Dict[str, Any] | None, key: str) -> float | None:
    if not statistics:
        return None
    percentiles = statistics.get("percentiles")
    if not isinstance(percentiles, dict):
        return None
    value = percentiles.get(key)
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

def parse_salaries(raw_items: List[Dict[str, Any]]) -> List[SalaryRecord]:
    """
    Convert raw salary dictionaries into structured SalaryRecord instances.
    """
    records: List[SalaryRecord] = []

    for item in raw_items:
        salary = item.get("salary") or {}
        currency = (salary.get("currency") or {}).get("code")
        base_stats = item.get("basePayStatistics") or {}
        total_stats = item.get("totalPayStatistics") or {}

        record = SalaryRecord(
            employer_id=(item.get("employer") or {}).get("id"),
            job_title=(salary.get("jobTitle") or {}).get("text") or "",
            currency_code=currency or "",
            salary_count=int(salary.get("salaryCount") or 0),
            base_pay_p10=_extract_percentile(base_stats, "p10"),
            base_pay_p25=_extract_percentile(base_stats, "p25"),
            base_pay_p50=_extract_percentile(base_stats, "p50"),
            base_pay_p75=_extract_percentile(base_stats, "p75"),
            base_pay_p90=_extract_percentile(base_stats, "p90"),
            total_pay_p10=_extract_percentile(total_stats, "p10"),
            total_pay_p25=_extract_percentile(total_stats, "p25"),
            total_pay_p50=_extract_percentile(total_stats, "p50"),
            total_pay_p75=_extract_percentile(total_stats, "p75"),
            total_pay_p90=_extract_percentile(total_stats, "p90"),
        )
        records.append(record)

    return records