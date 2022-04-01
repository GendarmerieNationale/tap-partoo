"""Partoo tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_partoo.streams import (
    BusinessesStream,
    GroupsStream,
    ReviewsStream,
)


class TapPartoo(Tap):
    """Partoo tap class."""

    name = "tap-partoo"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key", th.StringType, required=True, description="Partoo API Key"
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            required=True,
            description="Start syncing data from that date",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [
            BusinessesStream(tap=self),
            GroupsStream(tap=self),
            ReviewsStream(tap=self),
        ]
