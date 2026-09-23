from enum import Enum


class Oauth2TokenBodyType0GrantType(str, Enum):
    AUTHORIZATION_CODE = "authorization_code"

    def __str__(self) -> str:
        return str(self.value)
