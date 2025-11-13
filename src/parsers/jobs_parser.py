from typing import Any, Dict, List

from storage.schemas import JobRecord

def parse_jobs(raw_items: List[Dict[str, Any]]) -> List[JobRecord]:
    """
    Convert raw job dictionaries into structured JobRecord instances.
    """
    records: List[JobRecord] = []

    for item in raw_items:
        job = item.get("job") or {}
        adjusted_pay = job.get("payPeriodAdjustedPay") or {}

        record = JobRecord(
            employer_id=(item.get("employer") or {}).get("id"),
            job_title_text=job.get("jobTitleText") or "",
            location_name=job.get("locationName") or "",
            pay_currency=job.get("payCurrency"),
            pay_period=job.get("payPeriod"),
            pay_p10=float(adjusted_pay.get("p10")) if adjusted_pay.get("p10") is not None else None,
            pay_p90=float(adjusted_pay.get("p90")) if adjusted_pay.get("p90") is not None else None,
            seo_job_link=job.get("seoJobLink"),
        )
        records.append(record)

    return records