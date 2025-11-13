from typing import Any, Dict, List

from storage.schemas import InterviewRecord

def parse_interviews(raw_items: List[Dict[str, Any]]) -> List[InterviewRecord]:
    """
    Convert raw interview dictionaries into structured InterviewRecord instances.
    """
    records: List[InterviewRecord] = []

    for item in raw_items:
        interview = item.get("interview", {}) or {}
        location = interview.get("location") or {}
        stats = item.get("companyInterviewStats") or {}

        record = InterviewRecord(
            employer_id=(item.get("employer") or {}).get("id"),
            interview_id=interview.get("id"),
            experience=interview.get("experience"),
            difficulty=interview.get("difficulty"),
            process_description=interview.get("processDescription") or "",
            location_name=location.get("name") or "",
            interview_questions=[
                q.get("question") or ""
                for q in (interview.get("userQuestions") or [])
                if isinstance(q, dict)
            ],
            total_interview_count=int(stats.get("totalInterviewCount") or 0),
            experience_counts=stats.get("interviewExperienceCounts") or {},
        )
        records.append(record)

    return records