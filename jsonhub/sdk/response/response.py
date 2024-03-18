import requests


class Response:

    def __init__(self,
                 body: str | None = None,
                 code: int = 0,
                 total: int = 0,
                 ):
        self._body = body
        self._code: int = code
        self._total: int = total

    def code(self) -> int:
        return self._code

    def header(self) -> str:
        result = f"{self._code}"
        if self._total > 0:
            result += f" (total: {self._total})"
        return result

    def body(self) -> str | None:
        return self._body

    def get_total(self) -> int:
        return self._total

    def __str__(self):
        return f"{self.header()}\n{self.body()}"
