from abc import ABC

from jsonhub.sdk.data_type import DataType
from jsonhub.sdk.response.response import Response


class Mapper(ABC):

    def supported_type(self) -> DataType:
        pass

    def map(self, input_data: Response) -> list[object] | object:
        pass
