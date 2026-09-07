from enum import Enum


class Oauth2TokenExchangeBodyAudience(str, Enum):
    JSONHUB_API = "jsonhub-api"

    def __str__(self) -> str:
        return str(self.value)
