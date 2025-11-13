import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

from client.session_manager import SessionManager

logger = logging.getLogger(__name__)

class GlassdoorClient:
    """
    Thin abstraction over Glassdoor data fetching.

    In this demo implementation, data is loaded from a local JSON file
    (data/sample_output.json) to keep the project runnable without external
    network calls. In a production environment, this class would be
    responsible for HTTP requests, pagination, retries, and rate limiting.
    """

    COMMAND_TO_RECORD_TYPE = {
        "reviews": "review",
        "interviews": "interview",
        "salaries": "salary",
        "jobs": "job",
        "locations": "location",
        "benefits": "benefit",
        "culture": "culture",
    }

    def __init__(
        self,
        base_url: str,
        company_id: int,
        session_manager: SessionManager,
        data_path: Optional[Path] = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.company_id = company_id
        self.session_manager = session_manager
        if data_path is None: