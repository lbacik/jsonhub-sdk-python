from enum import Enum


class BaseFields(Enum):
    ID: str = "id"
    SLUG: str = "slug"

    DATA: str = "data"
    PARENT: str = "parent"
    DEFINITION: str = "definition"

    JSONSCHEMA: str = "jsonSchema"
    PARENT_ENTITY: str = "parentEntity"
