import json

from jsonhub.sdk.data_type import DataType
from jsonhub.sdk.entity import Entity
from jsonhub.sdk.response.mappers.abc_mapper import Mapper
from jsonhub.sdk.response.response import Response


class EntityMapper(Mapper):

    def supported_type(self) -> DataType:
        return DataType.ENTITY

    def map(self, input_data: Response) -> object:
        input_value = json.loads(input_data.body() or '{}')
        return Entity.create(input_value)
