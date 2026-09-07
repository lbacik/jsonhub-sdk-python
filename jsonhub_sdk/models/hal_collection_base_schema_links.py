from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hal_collection_base_schema_links_first import HalCollectionBaseSchemaLinksFirst
    from ..models.hal_collection_base_schema_links_last import HalCollectionBaseSchemaLinksLast
    from ..models.hal_collection_base_schema_links_next import HalCollectionBaseSchemaLinksNext
    from ..models.hal_collection_base_schema_links_previous import HalCollectionBaseSchemaLinksPrevious


T = TypeVar("T", bound="HalCollectionBaseSchemaLinks")


@_attrs_define
class HalCollectionBaseSchemaLinks:
    """
    Attributes:
        first (Union[Unset, HalCollectionBaseSchemaLinksFirst]):
        last (Union[Unset, HalCollectionBaseSchemaLinksLast]):
        next_ (Union[Unset, HalCollectionBaseSchemaLinksNext]):
        previous (Union[Unset, HalCollectionBaseSchemaLinksPrevious]):
    """

    first: Union[Unset, "HalCollectionBaseSchemaLinksFirst"] = UNSET
    last: Union[Unset, "HalCollectionBaseSchemaLinksLast"] = UNSET
    next_: Union[Unset, "HalCollectionBaseSchemaLinksNext"] = UNSET
    previous: Union[Unset, "HalCollectionBaseSchemaLinksPrevious"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.first, Unset):
            first = self.first.to_dict()

        last: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last, Unset):
            last = self.last.to_dict()

        next_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.next_, Unset):
            next_ = self.next_.to_dict()

        previous: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.previous, Unset):
            previous = self.previous.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first is not UNSET:
            field_dict["first"] = first
        if last is not UNSET:
            field_dict["last"] = last
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hal_collection_base_schema_links_first import HalCollectionBaseSchemaLinksFirst
        from ..models.hal_collection_base_schema_links_last import HalCollectionBaseSchemaLinksLast
        from ..models.hal_collection_base_schema_links_next import HalCollectionBaseSchemaLinksNext
        from ..models.hal_collection_base_schema_links_previous import HalCollectionBaseSchemaLinksPrevious

        d = dict(src_dict)
        _first = d.pop("first", UNSET)
        first: Union[Unset, HalCollectionBaseSchemaLinksFirst]
        if isinstance(_first, Unset):
            first = UNSET
        else:
            first = HalCollectionBaseSchemaLinksFirst.from_dict(_first)

        _last = d.pop("last", UNSET)
        last: Union[Unset, HalCollectionBaseSchemaLinksLast]
        if isinstance(_last, Unset):
            last = UNSET
        else:
            last = HalCollectionBaseSchemaLinksLast.from_dict(_last)

        _next_ = d.pop("next", UNSET)
        next_: Union[Unset, HalCollectionBaseSchemaLinksNext]
        if isinstance(_next_, Unset):
            next_ = UNSET
        else:
            next_ = HalCollectionBaseSchemaLinksNext.from_dict(_next_)

        _previous = d.pop("previous", UNSET)
        previous: Union[Unset, HalCollectionBaseSchemaLinksPrevious]
        if isinstance(_previous, Unset):
            previous = UNSET
        else:
            previous = HalCollectionBaseSchemaLinksPrevious.from_dict(_previous)

        hal_collection_base_schema_links = cls(
            first=first,
            last=last,
            next_=next_,
            previous=previous,
        )

        hal_collection_base_schema_links.additional_properties = d
        return hal_collection_base_schema_links

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
