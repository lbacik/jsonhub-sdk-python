import json

from dataclasses import dataclass


@dataclass
class Entity:
    id: str
    data: dict
    slug: str | None = None
    parent: str | None = None
    definition: str | None = None

    @staticmethod
    def create(data: dict) -> 'Entity':
        return Entity(
            id=data.get('id'),
            slug=data.get('slug', None),
            data=data.get('data'),
            definition=data.get('definition'),
            parent=data.get('parent', None),
        )
