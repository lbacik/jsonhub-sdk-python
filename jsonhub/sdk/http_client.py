from abc import ABC

from jsonhub.sdk.request.request import Request
from jsonhub.sdk.response.response import Response


class HttpClient(ABC):

    def execute_request(self, request: Request) -> Response:
        pass
