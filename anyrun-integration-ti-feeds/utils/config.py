import os
from uuid import UUID
from dotenv import load_dotenv

load_dotenv()


class Config:
    INTEGRATION: str = 'MISP:1.0.1'
    DATE_TIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'

    EVENT_UUID: UUID = UUID('c29f723b-4923-4356-aae7-4fe799f8965c')
    EVENT_DISTRIBUTION_LEVEL: int = int(os.environ.get('EVENT_DISTRIBUTION_LEVEL'))
    EVENT_ANALYSIS_STAGE: int = int(os.environ.get('EVENT_ANALYSIS_STAGE'))
    EVENT_THREAT_LEVEL_ID: int = int(os.environ.get('EVENT_THREAT_LEVEL_ID'))
    EVENT_PUBLISH: bool = True if os.environ.get('EVENT_PUBLISH') in (1, 'true', 'True') else False

    ORG_UUID: str = '7c25c6bf-bf00-45b4-852c-354a7616f7e1'
    ORG_NAME: str = 'ANY.RUN'

    MISP_URL: str = os.environ.get('MISP_URL')
    MISP_API_KEY: str = os.environ.get('MISP_API_KEY')
    MISP_VERIFY_SSL: bool = True if os.environ.get('MISP_VERIFY_SSL') in (1, 'true', 'True') else False
    MISP_CERT: str = os.environ.get('MISP_CERT')

    ANYRUN_FEED_FETCH_DEPTH: int = int(os.environ.get('ANYRUN_FEED_FETCH_DEPTH'))
    ANYRUN_FEED_FETCH_INTERVAL: int = int(os.environ.get('ANYRUN_FEED_FETCH_INTERVAL'))
    ANYRUN_BASIC_TOKEN: str = os.environ.get('ANYRUN_BASIC_TOKEN')
    LOGS_FILE_PATH: str = os.path.join(os.path.abspath('logs'), 'anyrun.logs')
