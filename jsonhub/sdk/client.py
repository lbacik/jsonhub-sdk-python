from jsonhub.sdk.data_type import DataType
from jsonhub.sdk.entity import Entity
from jsonhub.sdk.http_client import HttpClient
from jsonhub.sdk.request.request_factory import RequestFactory
from jsonhub.sdk.criteria.criteria import Criteria
from jsonhub.sdk.response.response import Response
from jsonhub.sdk.response.response_mapper import ResponseMapper


class Client:

    def __init__(self,
                 request_factory: RequestFactory,
                 http_client: HttpClient,
                 response_mapper: ResponseMapper = None,
                 ):
        self._requestFactory = request_factory
        self._httpClient = http_client
        self._responseMapper = response_mapper
        self._debug = False
        self._last_total = 0
        self._last_raw_response = None

    def set_debug(self, debug: bool = True) -> 'Client':
        self._debug = debug
        return self

    def get_entities(self, criteria: Criteria = None) -> list:
        # if criteria is None:
        #     criteria = Criteria()
        response: Response = self._process(DataType.ENTITIES, criteria)
        self._last_total = response.get_total()
        return (self._responseMapper
                .select_mapper(DataType.ENTITIES)
                .map(response))

    def get_entity(self, uuid: str) -> Entity | None:
        response: Response = self._process(DataType.ENTITY, uuid=uuid)
        result = (self._responseMapper
                  .select_mapper(DataType.ENTITY)
                  .map(response))
        self._last_total = 1 if result else 0
        return result

    # def add_entity(self, entity: Entity) -> Response:
    #     return self._process(DataType.ADD_ENTITY, entity)
    #
    # def update_entity(self, entity: Entity) -> Response:
    #     return self._process(DataType.UPDATE_ENTITY, entity)

    def get_definitions(self, criteria: Criteria = None) -> Response:
        # if criteria is None:
        #     criteria = Criteria()
        return self._process(DataType.SCHEMAS, criteria)

    def last_total(self) -> int:
        return self._last_total

    def _process(self, data_type: DataType, criteria: Criteria | None = None, uuid: str | None = None) -> Response:
        request = self._requestFactory.create(data_type, criteria, uuid)

        # TODO: fix this debug
        if self._debug:
            request.debug()

        response: Response = self._httpClient.execute_request(request)
        self._last_raw_response = self._httpClient._last_response;

        if response.code() >= 400:
            raise Exception(f'Error: {response.code()} - {response.body}')

        return response
