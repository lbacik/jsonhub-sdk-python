from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.constraint_violation_violations_item_payload import ConstraintViolationViolationsItemPayload


T = TypeVar("T", bound="ConstraintViolationViolationsItem")


@_attrs_define
class ConstraintViolationViolationsItem:
    """
    Attributes:
        property_path (str): The property path of the violation
        message (str): The message associated with the violation
        code (Union[Unset, str]): The code of the violation
        hint (Union[Unset, str]): An extra hint to understand the violation
        payload (Union[Unset, ConstraintViolationViolationsItemPayload]): The serialized payload of the violation
    """

    property_path: str
    message: str
    code: Union[Unset, str] = UNSET
    hint: Union[Unset, str] = UNSET
    payload: Union[Unset, "ConstraintViolationViolationsItemPayload"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_path = self.property_path

        message = self.message

        code = self.code

        hint = self.hint

        payload: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "propertyPath": property_path,
                "message": message,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if hint is not UNSET:
            field_dict["hint"] = hint
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.constraint_violation_violations_item_payload import ConstraintViolationViolationsItemPayload

        d = dict(src_dict)
        property_path = d.pop("propertyPath")

        message = d.pop("message")

        code = d.pop("code", UNSET)

        hint = d.pop("hint", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, ConstraintViolationViolationsItemPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = ConstraintViolationViolationsItemPayload.from_dict(_payload)

        constraint_violation_violations_item = cls(
            property_path=property_path,
            message=message,
            code=code,
            hint=hint,
            payload=payload,
        )

        constraint_violation_violations_item.additional_properties = d
        return constraint_violation_violations_item

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
