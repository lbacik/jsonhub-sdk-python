from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.constraint_violation_violations_item import ConstraintViolationViolationsItem


T = TypeVar("T", bound="ConstraintViolation")


@_attrs_define
class ConstraintViolation:
    """Unprocessable entity

    Attributes:
        status (Union[Unset, int]):  Default: 422.
        violations (Union[Unset, list['ConstraintViolationViolationsItem']]):
        detail (Union[Unset, str]):
        type_ (Union[Unset, str]):
        title (Union[None, Unset, str]):
        instance (Union[None, Unset, str]):
    """

    status: Union[Unset, int] = 422
    violations: Union[Unset, list["ConstraintViolationViolationsItem"]] = UNSET
    detail: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    instance: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        violations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.violations, Unset):
            violations = []
            for violations_item_data in self.violations:
                violations_item = violations_item_data.to_dict()
                violations.append(violations_item)

        detail = self.detail

        type_ = self.type_

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        instance: Union[None, Unset, str]
        if isinstance(self.instance, Unset):
            instance = UNSET
        else:
            instance = self.instance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if violations is not UNSET:
            field_dict["violations"] = violations
        if detail is not UNSET:
            field_dict["detail"] = detail
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title
        if instance is not UNSET:
            field_dict["instance"] = instance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.constraint_violation_violations_item import ConstraintViolationViolationsItem

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        violations = []
        _violations = d.pop("violations", UNSET)
        for violations_item_data in _violations or []:
            violations_item = ConstraintViolationViolationsItem.from_dict(violations_item_data)

            violations.append(violations_item)

        detail = d.pop("detail", UNSET)

        type_ = d.pop("type", UNSET)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_instance(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        instance = _parse_instance(d.pop("instance", UNSET))

        constraint_violation = cls(
            status=status,
            violations=violations,
            detail=detail,
            type_=type_,
            title=title,
            instance=instance,
        )

        constraint_violation.additional_properties = d
        return constraint_violation

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
