from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

@dataclass
class ReviewRecord:
    employer_id: Optional[int]
    employer_short_name: str
    employer_logo_url: Optional[str]
    review_id: Optional[int]
    review_datetime: Optional[datetime]
    summary: str
    pros: str
    cons: str
    employment_status: str
    is_current_job: bool
    job_title: str
    location_name: str
    language_id: str
    rating_overall: float
    rating_work_life_balance: float
    rating_compensation_and_benefits: float
    rating_culture_and_values: float
    rating_diversity_and_inclusion: float
    rating_career_opportunities: float
    rating_senior_leadership: float
    rating_recommend_to_friend: Optional[str]
    overall_company_rating: float
    overall_recommend_to_friend_rating: float
    overall_culture_and_values_rating: float
    overall_diversity_and_inclusion_rating: float
    all_reviews_count: int

@dataclass
class InterviewRecord:
    employer_id: Optional[int]
    interview_id: Optional[int]
    experience: Optional[str]
    difficulty: Optional[str]
    process_description: str
    location_name: str
    interview_questions: List[str]
    total_interview_count: int
    experience_counts: Dict[str, Any]

@dataclass
class SalaryRecord:
    employer_id: Optional[int]
    job_title: str
    currency_code: str
    salary_count: int
    base_pay_p10: Optional[float]
    base_pay_p25: Optional[float]
    base_pay_p50: Optional[float]
    base_pay_p75: Optional[float]
    base_pay_p90: Optional[float]
    total_pay_p10: Optional[float]
    total_pay_p25: Optional[float]
    total_pay_p50: Optional[float]
    total_pay_p75: Optional[float]
    total_pay_p90: Optional[float]

@dataclass
class JobRecord:
    employer_id: Optional[int]
    job_title_text: str
    location_name: str
    pay_currency: Optional[str]
    pay_period: Optional[str]
    pay_p10: Optional[float]
    pay_p90: Optional[float]
    seo_job_link: Optional[str]

@dataclass
class LocationRecord:
    employer_id: Optional[int]
    office_location_id: Optional[int]
    city_name: str
    country_name: str
    latitude: Optional[float]
    longitude: Optional[float]

@dataclass
class BenefitRecord:
    employer_id: Optional[int]
    rating: float
    user_entered_job_title: str
    city_name: str
    state_name: str
    comments: List[str]
    overall_benefit_rating: float
    total_benefit_reviews: int
    category_statistics: Dict[str, Any]

@dataclass
class CultureRecord:
    employer_id: Optional[int]
    category: str
    category_value: str
    overall_rating: float
    recommend_to_friend_rating: float