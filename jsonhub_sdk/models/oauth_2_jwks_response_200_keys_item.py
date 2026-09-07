from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Oauth2JwksResponse200KeysItem")


@_attrs_define
class Oauth2JwksResponse200KeysItem:
    """
    Attributes:
        kty (Union[Unset, str]):  Example: RSA.
        use (Union[Unset, str]):  Example: sig.
        kid (Union[Unset, str]):
        alg (Union[Unset, str]):  Example: RS256.
        n (Union[Unset, str]):
        e (Union[Unset, str]):
    """

    kty: Union[Unset, str] = UNSET
    use: Union[Unset, str] = UNSET
    kid: Union[Unset, str] = UNSET
    alg: Union[Unset, str] = UNSET
    n: Union[Unset, str] = UNSET
    e: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kty = self.kty

        use = self.use

        kid = self.kid

        alg = self.alg

        n = self.n

        e = self.e

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kty is not UNSET:
            field_dict["kty"] = kty
        if use is not UNSET:
            field_dict["use"] = use
        if kid is not UNSET:
            field_dict["kid"] = kid
        if alg is not UNSET:
            field_dict["alg"] = alg
        if n is not UNSET:
            field_dict["n"] = n
        if e is not UNSET:
            field_dict["e"] = e

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kty = d.pop("kty", UNSET)

        use = d.pop("use", UNSET)

        kid = d.pop("kid", UNSET)

        alg = d.pop("alg", UNSET)

        n = d.pop("n", UNSET)

        e = d.pop("e", UNSET)

        oauth_2_jwks_response_200_keys_item = cls(
            kty=kty,
            use=use,
            kid=kid,
            alg=alg,
            n=n,
            e=e,
        )

        oauth_2_jwks_response_200_keys_item.additional_properties = d
        return oauth_2_jwks_response_200_keys_item

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
