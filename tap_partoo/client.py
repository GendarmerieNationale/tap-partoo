"""REST client handling, including PartooStream base class."""

from typing import Any, Dict, Optional

import requests
from singer_sdk.authenticators import APIKeyAuthenticator
from singer_sdk.streams import RESTStream


class PartooStream(RESTStream):
    """Partoo stream class."""

    url_base = "https://api.partoo.co/v2"

    @property
    def records_jsonpath(self) -> str:
        return f"$.{self.name}[*]"

    @property
    def authenticator(self) -> APIKeyAuthenticator:
        """Return a new authenticator object."""
        return APIKeyAuthenticator.create_for_stream(
            self, key="x-APIKey", value=self.config.get("api_key"), location="header"
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        json_response = response.json()
        current_page = json_response["page"]
        max_page = json_response["max_page"]
        if current_page < max_page:
            return current_page + 1
        return None

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        if next_page_token:
            params["page"] = next_page_token
        if self.replication_key:
            # we are doing incremental sync
            # todo: should i really take the update_date in the context??
            #   https://sdk.meltano.com/en/latest/implementation/state.html
            # params["update_date__gte"] = stream_state["update_date"]
            # params["sort"] = "asc"
            # params["order_by"] = self.replication_key
            pass
        return params


