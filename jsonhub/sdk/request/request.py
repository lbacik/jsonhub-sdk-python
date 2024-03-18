import requests

from jsonhub.sdk.request.http_method import HttpMethod


class Request:

    def __init__(self,
                 url: str,
                 method: HttpMethod = HttpMethod.GET,
                 params: dict | None = None,
                 headers: dict | None = None,
                 body: dict | None = None,
                 ):
        self._url = url
        self._params = params
        self._method = method
        self._headers = headers
        self._body = body

    def url(self) -> str:
        return self._url

    def method_name(self) -> str:
        return self._method.value

    def params(self) -> dict | None:
        return self._params

    def headers(self) -> dict | None:
        return self._headers

    def body(self) -> dict | None:
        return self._body

    # def execute(self) -> requests.Response | None:
    #     result = None
    #     try:
    #         result = requests.request(
    #             method=self._method.value,
    #             url=self._url,
    #             params=self._params,
    #             headers=self._headers,
    #             json=self._body,
    #         )
    #     except requests.RequestException as e:
    #         print(f"Request failed: {e}")
    #
    #     return result

    def debug(self):
        print(f"URL: {self._url}")
        print(f"Method: {self._method.value}")
        print(f"Params: {self._params}")
        print(f"Headers: {self._headers}")
        print(f"Body: {self._body}")
