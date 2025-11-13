from typing import Any, Dict, List

from storage.schemas import LocationRecord

def parse_locations(raw_items: List[Dict[str, Any]]) -> List[LocationRecord]:
    """
    Convert raw office location dictionaries into structured LocationRecord instances.
    """
    records: List[LocationRecord] = []

    for item in raw_items:
        office = item.get("officeLocation") or {}

        record = LocationRecord(
            employer_id=(item.get("employer") or {}).get("id"),
            office_location_id=office.get("id"),
            city_name=office.get("cityName") or "",
            country_name=office.get("countryName") or "",
            latitude=float(office.get("latitude")) if office.get("latitude") is not None else None,
            longitude=float(office.get("longitude")) if office.get("longitude") is not None else None,
        )
        records.append(record)

    return records