"""Stream type classes for tap-partoo."""

from pathlib import Path

from tap_partoo.client import PartooStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class BusinessesStream(PartooStream):
    name = "businesses"
    path = "/business/search"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "businesses.json"


class GroupsStream(PartooStream):
    name = "groups"
    path = "/groups"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "groups.json"


class ReviewsStream(PartooStream):
    name = "reviews"
    path = "/reviews"
    primary_keys = ["id"]
    replication_key = "update_date"  # use Partoo 'update_date' for incremental loading
    schema_filepath = SCHEMAS_DIR / "reviews.json"
