import uuid
from datetime import datetime, UTC

from pymisp import MISPEvent, MISPOrganisation, PyMISP, MISPObject

from utils.config import Config
from utils.logs import FileLoggingManager

logger = FileLoggingManager()


class MISP:
    def __init__(self):
        self._misp_api = PyMISP(
            url=Config.MISP_URL,
            key=Config.MISP_API_KEY,
            ssl=Config.MISP_VERIFY_SSL,
            cert=Config.MISP_CERT
        )

    def create_or_update_event(
        self,
        feeds: list[dict],
        date: datetime = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
    ) -> None:
        event_info = f'ANY.RUN TI Feeds: {date}'

        self._renew_event(event_info)
        self._enrich_event(feeds)

        if self._is_event_exists(event_info):
            logger.info(f'MISP Event is successfully updated.')
            self._misp_api.update_event(self._event)
        else:
            self._misp_api.add_event(self._event)
            logger.info(f'MISP Event is successfully created.')

    def _renew_event(self, event_info: str) -> None:
        self._event = MISPEvent()
        self._event.info = event_info
        self._event.orgc = self._create_organization()
        self._event.uuid = str(uuid.uuid5(Config.EVENT_UUID, event_info))
        self._event.distribution = Config.EVENT_DISTRIBUTION_LEVEL
        self._event.analysis = Config.EVENT_ANALYSIS_STAGE
        self._event.threat_level_id = Config.EVENT_THREAT_LEVEL_ID
        self._event.timestamp = datetime.now(UTC)
        self._event.add_tag(f'ANY.RUN TI Feeds')

        if Config.EVENT_PUBLISH:
            self._event.publish()

    def _enrich_event(self, feeds: list[dict]):
        logger.info(f'Received {len(feeds)} feeds.')
        for feed in feeds:
            feed_type, feed_value = self._extract_feed_data(feed)

            obj = MISPObject({'ip': 'ip-port', 'domain': 'domain-ip', 'url': 'url'}.get(feed_type))

            obj.add_attribute(
                feed_type,
                to_ids=True,
                value=feed_value,
                first_seen=feed.get('created'),
                last_seen=feed.get('modified'),
                categories='Network activity',
                Tag=self._add_tags(feed),
            )

            if references := feed.get('external_references'):
                self._add_references(obj, references[-1])

            self._event.add_object(obj)

    def _is_event_exists(self, event_info: str) -> bool:
        if self._misp_api.search(controller="events", eventinfo=event_info):
            return True

    @staticmethod
    def _add_tags(feed: dict) -> list[str]:
        tags = []

        score = feed.get('confidence')
        tags.append(f'anyrun-feeds:score="{score}"')

        if labels := feed.get('labels'):
            for label in labels:
                tags.append(f'anyrun-feeds:label="{label}"')

        return tags

    @staticmethod
    def _add_references(obj: MISPObject, reference: dict) -> None:
        obj.add_attribute(
            'text',
            type='text',
            value=reference.get('source_name'),
            categories='Other'
        )

        obj.add_attribute(
            'text',
            type='link',
            value=reference.get('url'),
            categories='External analysis'
        )

    @staticmethod
    def _create_organization() -> MISPOrganisation:
        organization = MISPOrganisation()
        organization.name = Config.ORG_NAME
        organization.uuid = Config.ORG_UUID

        return organization

    @staticmethod
    def _extract_feed_data(feed: dict) -> tuple[str, str]:
        """
        Extracts indicator type, value using raw indicator

        :param feed: Raw ANY.RUN indicator
        :return: ANY.RUN indicator type, ANY.RUN indicator value
        """
        pattern = feed.get("pattern", "")
        feed_type = pattern.split(":")[0][1:]
        feed_value = pattern.split(" = '")[1][:-2]

        return {'domain-name': 'domain', 'ipv4-addr': 'ip', 'url': 'url'}.get(feed_type), feed_value
