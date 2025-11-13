from datetime import datetime
from typing import Any, Dict, List

from storage.schemas import ReviewRecord

def _parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None

def parse_reviews(raw_items: List[Dict[str, Any]]) -> List[ReviewRecord]:
    """
    Convert raw review dictionaries into structured ReviewRecord instances.
    """
    records: List[ReviewRecord] = []

    for item in raw_items:
        employer = item.get("employer", {})
        stats = item.get("companyReviewStats", {}).get("ratings", {})

        record = ReviewRecord(
            employer_id=employer.get("id"),
            employer_short_name=employer.get("shortName"),
            employer_logo_url=employer.get("squareLogoUrl"),
            review_id=item.get("reviewId"),
            review_datetime=_parse_datetime(item.get("reviewDateTime")),
            summary=item.get("summary") or "",
            pros=item.get("pros") or "",
            cons=item.get("cons") or "",
            employment_status=item.get("employmentStatus") or "",
            is_current_job=bool(item.get("isCurrentJob")),
            job_title=(item.get("jobTitle") or {}).get("text") or "",
            location_name=(item.get("location") or {}).get("name") or "",
            language_id=item.get("languageId") or "",
            rating_overall=float(item.get("ratingOverall") or 0),
            rating_work_life_balance=float(item.get("ratingWorkLifeBalance") or 0),
            rating_compensation_and_benefits=float(
                item.get("ratingCompensationAndBenefits") or 0
            ),
            rating_culture_and_values=float(
                item.get("ratingCultureAndValues") or 0
            ),
            rating_diversity_and_inclusion=float(
                item.get("ratingDiversityAndInclusion") or 0
            ),
            rating_career_opportunities=float(
                item.get("ratingCareerOpportunities") or 0
            ),
            rating_senior_leadership=float(
                item.get("ratingSeniorLeadership") or 0
            ),
            rating_recommend_to_friend=item.get("ratingRecommendToFriend"),
            overall_company_rating=float(stats.get("overallRating") or 0),
            overall_recommend_to_friend_rating=float(
                stats.get("recommendToFriendRating") or 0
            ),
            overall_culture_and_values_rating=float(
                stats.get("cultureAndValuesRating") or 0
            ),
            overall_diversity_and_inclusion_rating=float(
                stats.get("diversityAndInclusionRating") or 0
            ),
            all_reviews_count=int(
                (item.get("companyReviewStats") or {}).get("allReviewsCount") or 0
            ),
        )
        records.append(record)

    return records