from jsonhub.sdk.data_type import DataType
from jsonhub.sdk.response.mappers.abc_mapper import Mapper
from jsonhub.sdk.response.response import Response


class ResponseMapper:

    def __init__(self, mappers: list):
        self._mappers = mappers

    def map(self, input_data: Response, output_type: DataType) -> list[object] | object | None:
        for mapper in self._mappers:
            if mapper.supported_type() == output_type:
                return mapper.map(input_data)

        raise ValueError(f'No mapper found for type {output_type}')

    def select_mapper(self, data_type: DataType) -> Mapper:
        for mapper in self._mappers:
            if mapper.supported_type() == data_type:
                return mapper

        raise ValueError(f'No mapper found for type {data_type}')