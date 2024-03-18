from jsonhub.infrastructure.http_client import HttpClient
from jsonhub.sdk.client import Client
from jsonhub.sdk.config import Config
from jsonhub.sdk.request.request_factory import RequestFactory
from jsonhub.sdk.response.mappers.entity import EntityMapper
from jsonhub.sdk.response.mappers.entities import EntitiesMapper
from jsonhub.sdk.response.response_mapper import ResponseMapper


class ClientFactory:

    @staticmethod
    def create(config: Config) -> Client:
        return Client(
            RequestFactory(config),
            HttpClient(),
            ResponseMapper([
                EntityMapper(),
                EntitiesMapper(),
            ])
        )
