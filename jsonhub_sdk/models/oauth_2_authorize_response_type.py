from enum import Enum


class Oauth2AuthorizeResponseType(str, Enum):
    CODE = "code"

    def __str__(self) -> str:
        return str(self.value)
