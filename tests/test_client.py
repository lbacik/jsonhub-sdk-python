import pytest
import json

from jsonhub.sdk.client import Client
from jsonhub.sdk.config import Config
from jsonhub.sdk.http_client import HttpClient
from jsonhub.sdk.request.request import Request
from jsonhub.sdk.request.request_factory import RequestFactory
from jsonhub.sdk.response.mappers.entities import EntitiesMapper
from jsonhub.sdk.response.mappers.entity import EntityMapper
from jsonhub.sdk.response.raw_response import RawResponse
from jsonhub.sdk.response.response import Response
from jsonhub.sdk.response.response_mapper import ResponseMapper


@pytest.fixture
def config() -> Config:
    return Config(
        'http://foo.bar',
    )


@pytest.fixture
def http_client(request) -> HttpClient:
    marker_return_code = request.node.get_closest_marker('return_code')
    marker_payload = request.node.get_closest_marker('payload')

    class MockHttpClient(HttpClient):
        def __init__(self):
            self._last_response = None

        def execute_request(self, request: Request) -> Response:
            return RawResponse(marker_return_code.args[0], marker_payload.args[0])

    return MockHttpClient()


@pytest.fixture
def create_client(config: Config, http_client: HttpClient) -> Client:
    return Client(
        RequestFactory(config),
        http_client,
        ResponseMapper([
            EntityMapper(),
            EntitiesMapper(),
        ])
    )


@pytest.mark.return_code(404)
@pytest.mark.payload('')
def test_get_entity_404(create_client: Client):
    with pytest.raises(Exception) as e:
        create_client.get_entity('123')


@pytest.mark.return_code(200)
@pytest.mark.payload(json.loads('{"id": "123", "data": {"foo": "bar"}}'))
def test_get_entity(create_client: Client):
    entity = create_client.get_entity('123')
    assert entity.id == '123'
    assert create_client.last_total() == 1


@pytest.mark.return_code(404)
@pytest.mark.payload('')
def test_get_entities_404(create_client: Client):
    with pytest.raises(Exception) as e:
        create_client.get_entities()


@pytest.mark.return_code(200)
@pytest.mark.payload(json.loads('{"hydra:totalItems":1,"hydra:member":[{"id": "123", "data": {"foo": "bar"}}]}'))
def test_get_entities(create_client: Client):
    entities = create_client.get_entities()
    assert len(list(entities)) == 1
    assert create_client.last_total() == 1
