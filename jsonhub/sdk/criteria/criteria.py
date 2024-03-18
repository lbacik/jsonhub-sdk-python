from dataclasses import dataclass
from jsonhub.sdk.criteria.base_fields import BaseFields
from jsonhub.sdk.data_type import DataType


@dataclass
class Criteria:
    # id: str | None = None
    fields: list[BaseFields] | None = None
    limit: int = 10
    page: int = 1
    parent: str | None = None
    definition: str | None = None

    def to_dict(self, data_type: DataType) -> dict | None:
        result = {}

        if data_type in [DataType.ENTITIES, DataType.SCHEMAS] and self.limit:
            result['limit'] = self.limit

        if data_type in [DataType.ENTITIES, DataType.SCHEMAS] and self.page:
            result['page'] = self.page

        if self.fields:
            result['properties[]'] = [field.value for field in self.fields]

        if self.parent:
            result['parent'] = self.parent

        if self.definition:
            result['definition'] = self.definition

        if len(result) > 0:
            return result

        return None
