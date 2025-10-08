import sys
from datetime import datetime, UTC
from loguru import logger

from utils.config import Config


class FileLoggingManager:
    """Implements saving logs to the text file"""

    def __init__(self):
        self.logger = logger

        self.logger.configure(
            handlers=[
                {
                    'sink': sys.stdout,
                    'format': '{extra[datetime]} | {level} | {message}',
                },
                {
                    'sink': Config.LOGS_FILE_PATH,
                    'format': '{extra[datetime]} | {level} | {message}',
                }
            ],
            extra={
                'retention': '1 month',
                'rotation': '1 week'
            },
            patcher=self._patch_timezone
        )

    @staticmethod
    def _patch_timezone(record):
        record['extra']['datetime'] = datetime.now(UTC)

    @staticmethod
    def info(message: str) -> None:
        logger.info(message)

    @staticmethod
    def warning(message: str) -> None:
        logger.warning(message)

    @staticmethod
    def error(message: str) -> None:
        logger.error(message)