from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hal_collection_base_schema_no_pagination_embedded_type_0 import (
        HalCollectionBaseSchemaNoPaginationEmbeddedType0,
    )
    from ..models.hal_collection_base_schema_no_pagination_embedded_type_1 import (
        HalCollectionBaseSchemaNoPaginationEmbeddedType1,
    )
    from ..models.hal_collection_base_schema_no_pagination_links import HalCollectionBaseSchemaNoPaginationLinks


T = TypeVar("T", bound="ApiMeapiTokensGetCollectionResponse200")


@_attrs_define
class ApiMeapiTokensGetCollectionResponse200:
    """personal.access.token.jsonhal-personal_access_token.read collection.

    Attributes:
        field_embedded (Union['HalCollectionBaseSchemaNoPaginationEmbeddedType0',
            'HalCollectionBaseSchemaNoPaginationEmbeddedType1']):
        field_links (HalCollectionBaseSchemaNoPaginationLinks):
        total_items (Union[Unset, int]):
        items_per_page (Union[Unset, int]):
    """

    field_embedded: Union[
        "HalCollectionBaseSchemaNoPaginationEmbeddedType0", "HalCollectionBaseSchemaNoPaginationEmbeddedType1"
    ]
    field_links: "HalCollectionBaseSchemaNoPaginationLinks"
    total_items: Union[Unset, int] = UNSET
    items_per_page: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hal_collection_base_schema_no_pagination_embedded_type_0 import (
            HalCollectionBaseSchemaNoPaginationEmbeddedType0,
        )

        field_embedded: dict[str, Any]
        if isinstance(self.field_embedded, HalCollectionBaseSchemaNoPaginationEmbeddedType0):
            field_embedded = self.field_embedded.to_dict()
        else:
            field_embedded = self.field_embedded.to_dict()

        field_links = self.field_links.to_dict()

        total_items = self.total_items

        items_per_page = self.items_per_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_embedded": field_embedded,
                "_links": field_links,
            }
        )
        if total_items is not UNSET:
            field_dict["totalItems"] = total_items
        if items_per_page is not UNSET:
            field_dict["itemsPerPage"] = items_per_page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hal_collection_base_schema_no_pagination_embedded_type_0 import (
            HalCollectionBaseSchemaNoPaginationEmbeddedType0,
        )
        from ..models.hal_collection_base_schema_no_pagination_embedded_type_1 import (
            HalCollectionBaseSchemaNoPaginationEmbeddedType1,
        )
        from ..models.hal_collection_base_schema_no_pagination_links import HalCollectionBaseSchemaNoPaginationLinks

        d = dict(src_dict)

        def _parse_field_embedded(
            data: object,
        ) -> Union[
            "HalCollectionBaseSchemaNoPaginationEmbeddedType0", "HalCollectionBaseSchemaNoPaginationEmbeddedType1"
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_embedded_type_0 = HalCollectionBaseSchemaNoPaginationEmbeddedType0.from_dict(data)

                return field_embedded_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            field_embedded_type_1 = HalCollectionBaseSchemaNoPaginationEmbeddedType1.from_dict(data)

            return field_embedded_type_1

        field_embedded = _parse_field_embedded(d.pop("_embedded"))

        field_links = HalCollectionBaseSchemaNoPaginationLinks.from_dict(d.pop("_links"))

        total_items = d.pop("totalItems", UNSET)

        items_per_page = d.pop("itemsPerPage", UNSET)

        api_meapi_tokens_get_collection_response_200 = cls(
            field_embedded=field_embedded,
            field_links=field_links,
            total_items=total_items,
            items_per_page=items_per_page,
        )

        api_meapi_tokens_get_collection_response_200.additional_properties = d
        return api_meapi_tokens_get_collection_response_200

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
