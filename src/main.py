import argparse
import json
import logging
import os
from pathlib import Path
from typing import Any, Dict, List

from client.glassdoor_client import GlassdoorClient
from client.session_manager import SessionManager
from parsers.reviews_parser import parse_reviews
from parsers.interviews_parser import parse_interviews
from parsers.salaries_parser import parse_salaries
from parsers.jobs_parser import parse_jobs
from parsers.locations_parser import parse_locations
from parsers.benefits_parser import parse_benefits
from parsers.culture_parser import parse_culture
from storage.exporters import export_records_to_jsonl, export_summary_to_stdout

logger = logging.getLogger("glassdoor_scraper")

COMMAND_TO_PARSER = {
    "reviews": parse_reviews,
    "interviews": parse_interviews,
    "salaries": parse_salaries,
    "jobs": parse_jobs,
    "locations": parse_locations,
    "benefits": parse_benefits,
    "culture": parse_culture,
}

def setup_logging() -> None:
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(
        level=getattr(logging, log_level, logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    )

def load_config(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def run_from_config(config: Dict[str, Any]) -> None:
    company_id = config.get("companyId")
    if company_id is None:
        raise ValueError("Config must contain 'companyId'")

    commands = config.get("commands") or ["reviews"]
    max_items = config.get("maxItems")
    output_dir = Path(config.get("outputDir", "data")).resolve()

    session_settings = config.get("session", {})
    session_manager = SessionManager(
        max_concurrency=session_settings.get("maxConcurrency", 2),
        min_concurrency=session_settings.get("minConcurrency", 1),
        max_request_retries=session_settings.get("maxRequestRetries", 3),
    )

    base_url = config.get("baseUrl", "https://www.glassdoor.com")
    client = GlassdoorClient(
        base_url=base_url,
        company_id=company_id,
        session_manager=session_manager,
    )

    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info("Starting run for company_id=%s commands=%s", company_id, commands)

    for command in commands:
        parser_fn = COMMAND_TO_PARSER.get(command)
        if parser_fn is None:
            logger.warning("Unknown command '%s' - skipping", command)
            continue

        logger.info("Fetching raw data for command='%s'", command)
        raw_items = client.fetch(command=command, max_items=max_items)

        logger.info("Parsing %d raw items for command='%s'", len(raw_items), command)
        parsed_records = parser_fn(raw_items)

        logger.info(
            "Parsed %d records for command='%s'", len(parsed_records), command
        )

        output_path = output_dir / f"{command}.jsonl"
        export_records_to_jsonl(parsed_records, output_path)
        export_summary_to_stdout(command, parsed_records)

    logger.info("Run complete.")

def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Glassdoor Scraper (Pay Per Result) - Local runner"
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        default="data/input.sample.json",
        help="Path to JSON config file (default: data/input.sample.json)",
    )
    return parser.parse_args(argv)

def main() -> None:
    setup_logging()
    args = parse_args()
    config_path = Path(args.input).resolve()
    logger.info("Loading config from %s", config_path)
    config = load_config(config_path)
    run_from_config(config)

if __name__ == "__main__":
    main()