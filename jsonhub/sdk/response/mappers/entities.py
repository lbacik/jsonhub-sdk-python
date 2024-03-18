import json

from jsonhub.sdk.data_type import DataType
from jsonhub.sdk.entity import Entity
from jsonhub.sdk.response.mappers.abc_mapper import Mapper
from jsonhub.sdk.response.response import Response


class EntitiesMapper(Mapper):
    def supported_type(self) -> DataType:
        return DataType.ENTITIES

    def map(self, input_data: Response) -> list[object]:
        input_value = json.loads(input_data.body() or '[]')
        return [Entity.create(item) for item in input_value]
