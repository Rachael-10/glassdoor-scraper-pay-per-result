from typing import Any, Dict, List

from storage.schemas import CultureRecord

def parse_culture(raw_items: List[Dict[str, Any]]) -> List[CultureRecord]:
    """
    Convert raw culture and demographic dictionaries into structured CultureRecord instances.
    """
    records: List[CultureRecord] = []

    for item in raw_items:
        culture = item.get("cultureDemographic") or {}
        ratings = culture.get("ratings") or {}

        record = CultureRecord(
            employer_id=(item.get("employer") or {}).get("id"),
            category=culture.get("category") or "",
            category_value=culture.get("categoryValue") or "",
            overall_rating=float(ratings.get("overallRating") or 0),
            recommend_to_friend_rating=float(
                ratings.get("recommendToFriendRating") or 0
            ),
        )
        records.append(record)

    return records