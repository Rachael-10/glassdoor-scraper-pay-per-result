from typing import Any, Dict, List

from storage.schemas import BenefitRecord

def parse_benefits(raw_items: List[Dict[str, Any]]) -> List[BenefitRecord]:
    """
    Convert raw benefit dictionaries into structured BenefitRecord instances.
    """
    records: List[BenefitRecord] = []

    for item in raw_items:
        benefits = item.get("benefits") or {}
        city = (benefits.get("city") or {}).get("name") or ""
        state = (benefits.get("state") or {}).get("name") or ""
        benefit_comments = item.get("benefitComments") or []
        stats = item.get("companyBenefitStats") or {}

        record = BenefitRecord(
            employer_id=(item.get("employer") or {}).get("id"),
            rating=float(benefits.get("rating") or 0),
            user_entered_job_title=benefits.get("userEnteredJobTitle") or "",
            city_name=city,
            state_name=state,
            comments=[
                c.get("comment") or ""
                for c in benefit_comments
                if isinstance(c, dict)
            ],
            overall_benefit_rating=float(stats.get("overallBenefitRating") or 0),
            total_benefit_reviews=int(stats.get("totalBenefitReviews") or 0),
            category_statistics=item.get("benefitsCategoryToStatisticAggregates") or {},
        )
        records.append(record)

    return records