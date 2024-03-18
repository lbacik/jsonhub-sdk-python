import requests

from jsonhub.sdk.http_client import HttpClient as AbstractHttpClient
from jsonhub.sdk.request.request import Request
from jsonhub.sdk.response.raw_response import RawResponse
from jsonhub.sdk.response.response import Response


class HttpClient(AbstractHttpClient):

    def __init__(self):
        self._last_response = None

    def execute_request(self, request: Request) -> Response:
        response: requests.Response = requests.request(
            method=request.method_name(),
            url=request.url(),
            params=request.params(),
            headers=request.headers(),
            json=request.body(),
        )

        self._last_response = response

        return RawResponse(
            response.status_code,
            response.json(),
        )
