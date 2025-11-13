import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class SessionManager:
    """
    Keeps track of concurrency and retry settings.

    In a production scraper this would manage HTTP sessions, connection pools,
    backoff strategies, and rate limiting. Here it primarily serves as a
    configuration container and hook for future extensions.
    """

    max_concurrency: int = 2
    min_concurrency: int = 1
    max_request_retries: int = 3

    def describe(self) -> str:
        desc = (
            f"SessionManager(max_concurrency={self.max_concurrency}, "
            f"min_concurrency={self.min_concurrency}, "
            f"max_request_retries={self.max_request_retries})"
        )
        logger.debug("Session configuration: %s", desc)
        return desc