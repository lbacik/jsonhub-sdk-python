from jsonhub.sdk.config import Config
from jsonhub.sdk.criteria.criteria import Criteria
from jsonhub.sdk.data_type import DataType
from jsonhub.sdk.request.http_method import HttpMethod
from jsonhub.sdk.request.request import Request


class RequestFactory:

    def __init__(self, config: Config):
        self._config = config

    def create(self, data_type: DataType, criteria: Criteria | None, uuid: str | None) -> Request:

        (url, method) = self._get_address(data_type, uuid)

        if criteria is not None:
            params = self._get_params(data_type, criteria)
        else:
            params = None

        return Request(
            url=url,
            method=method,
            params=params,
            headers=self._get_headers(),
        )

    def _get_address(self, data_type: DataType, uuid: str | None) -> tuple[str, HttpMethod]:

        match data_type:
            case DataType.ENTITIES:
                return self._method_address('entities'), HttpMethod.GET
            case DataType.SCHEMAS:
                return self._method_address('definitions'), HttpMethod.GET
            case DataType.ENTITY:
                if uuid is None:
                    raise ValueError('UUID is required for entity')
                return self._method_address(f'entities/{uuid}'), HttpMethod.GET
            case DataType.SCHEMA:
                if uuid is None:
                    raise ValueError('UUID is required for schema')
                return self._method_address(f'definitions/{uuid}'), HttpMethod.GET
            case _:
                raise ValueError(f"Unknown data type: {data_type}")

    def _method_address(self, path: str):
        return '%s/%s' % (self._config.api_url, path)

    @staticmethod
    def _get_params(data_type: DataType, criteria: Criteria) -> dict | None:
        return criteria.to_dict(data_type)

    @staticmethod
    def _get_headers() -> dict:
        return {
            'Accept': 'application/ld+json',
            'Content-Type': 'application/ld+json',
        }
