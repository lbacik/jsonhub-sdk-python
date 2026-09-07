from enum import Enum


class Oauth2AuthorizeCodeChallengeMethod(str, Enum):
    S256 = "S256"

    def __str__(self) -> str:
        return str(self.value)
