from enum import Enum


class HttpMethod(Enum):
    GET: str = "GET"
    POST: str = "POST"
    PATCH: str = "PATCH"
    DELETE: str = "DELETE"
