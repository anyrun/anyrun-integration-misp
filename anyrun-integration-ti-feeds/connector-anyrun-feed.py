import time
from datetime import UTC, datetime, timedelta

import urllib3
from anyrun.connectors import FeedsConnector
from anyrun.iterators import FeedsIterator
from utils.config import Config
from utils.logs import FileLoggingManager
from utils.misp import MISP

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = FileLoggingManager()


def main() -> None:
    misp = MISP()

    connector_config = {
        "api_key": Config.ANYRUN_API_KEY,
        "integration": Config.INTEGRATION,
    }

    if Config.HTTP_PROXY:
        connector_config["proxy"] = Config.HTTP_PROXY

    with FeedsConnector(**connector_config) as connector:
        while True:
            logger.info("Initialized Feeds enrichment.")
            for feeds in FeedsIterator.taxii_stix(
                connector,
                chunk_size=500,
                limit=500,
                modified_after=(
                    datetime.now(UTC) - timedelta(days=Config.ANYRUN_FEED_FETCH_DEPTH)
                ).strftime(Config.DATE_TIME_FORMAT),
            ):
                misp.create_or_update_event(feeds)

            logger.info(
                f"Feeds enrichment is successfully ended. Next run at: "
                f"{datetime.now(UTC) + timedelta(minutes=Config.ANYRUN_FEED_FETCH_INTERVAL)}"
            )

            time.sleep(Config.ANYRUN_FEED_FETCH_INTERVAL * 60)


if __name__ == "__main__":
    main()
