from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.current_user_limit_usage import CurrentUserLimitUsage


T = TypeVar("T", bound="CurrentUserLimits")


@_attrs_define
class CurrentUserLimits:
    """
    Attributes:
        entities (CurrentUserLimitUsage):
        root_entities (CurrentUserLimitUsage):
        private_entities (CurrentUserLimitUsage):
        definitions (CurrentUserLimitUsage):
    """

    entities: "CurrentUserLimitUsage"
    root_entities: "CurrentUserLimitUsage"
    private_entities: "CurrentUserLimitUsage"
    definitions: "CurrentUserLimitUsage"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entities = self.entities.to_dict()

        root_entities = self.root_entities.to_dict()

        private_entities = self.private_entities.to_dict()

        definitions = self.definitions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entities": entities,
                "rootEntities": root_entities,
                "privateEntities": private_entities,
                "definitions": definitions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.current_user_limit_usage import CurrentUserLimitUsage

        d = dict(src_dict)
        entities = CurrentUserLimitUsage.from_dict(d.pop("entities"))

        root_entities = CurrentUserLimitUsage.from_dict(d.pop("rootEntities"))

        private_entities = CurrentUserLimitUsage.from_dict(d.pop("privateEntities"))

        definitions = CurrentUserLimitUsage.from_dict(d.pop("definitions"))

        current_user_limits = cls(
            entities=entities,
            root_entities=root_entities,
            private_entities=private_entities,
            definitions=definitions,
        )

        current_user_limits.additional_properties = d
        return current_user_limits

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
