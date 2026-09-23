from enum import Enum


class Oauth2RevokeBodyTokenTypeHint(str, Enum):
    ACCESS_TOKEN = "access_token"
    REFRESH_TOKEN = "refresh_token"

    def __str__(self) -> str:
        return str(self.value)
