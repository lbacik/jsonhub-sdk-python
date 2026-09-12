from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Oauth2MetadataResponse200")


@_attrs_define
class Oauth2MetadataResponse200:
    """
    Attributes:
        issuer (Union[Unset, str]):  Example: https://jsonhub.example.
        authorization_endpoint (Union[Unset, str]):  Example: https://jsonhub.example/oauth2/authorize.
        token_endpoint (Union[Unset, str]):  Example: https://jsonhub.example/oauth2/token.
        jwks_uri (Union[Unset, str]):  Example: https://jsonhub.example/oauth2/jwks.
        registration_endpoint (Union[Unset, str]):  Example: https://jsonhub.example/oauth2/register.
        revocation_endpoint (Union[Unset, str]):  Example: https://jsonhub.example/oauth2/revoke.
        token_exchange_endpoint (Union[Unset, str]):  Example: https://jsonhub.example/oauth2/token-exchange.
        response_types_supported (Union[Unset, list[str]]):  Example: ['code'].
        grant_types_supported (Union[Unset, list[str]]):  Example: ['authorization_code', 'urn:ietf:params:oauth:grant-
            type:token-exchange'].
        code_challenge_methods_supported (Union[Unset, list[str]]):  Example: ['S256'].
        audiences_supported (Union[Unset, list[str]]):  Example: ['jsonhub-api'].
        scopes_supported (Union[Unset, list[str]]):  Example: ['mcp', 'frontend', 'jsonhub:entities:read',
            'jsonhub:entities:write', 'jsonhub:definitions:write'].
    """

    issuer: Union[Unset, str] = UNSET
    authorization_endpoint: Union[Unset, str] = UNSET
    token_endpoint: Union[Unset, str] = UNSET
    jwks_uri: Union[Unset, str] = UNSET
    registration_endpoint: Union[Unset, str] = UNSET
    revocation_endpoint: Union[Unset, str] = UNSET
    token_exchange_endpoint: Union[Unset, str] = UNSET
    response_types_supported: Union[Unset, list[str]] = UNSET
    grant_types_supported: Union[Unset, list[str]] = UNSET
    code_challenge_methods_supported: Union[Unset, list[str]] = UNSET
    audiences_supported: Union[Unset, list[str]] = UNSET
    scopes_supported: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issuer = self.issuer

        authorization_endpoint = self.authorization_endpoint

        token_endpoint = self.token_endpoint

        jwks_uri = self.jwks_uri

        registration_endpoint = self.registration_endpoint

        revocation_endpoint = self.revocation_endpoint

        token_exchange_endpoint = self.token_exchange_endpoint

        response_types_supported: Union[Unset, list[str]] = UNSET
        if not isinstance(self.response_types_supported, Unset):
            response_types_supported = self.response_types_supported

        grant_types_supported: Union[Unset, list[str]] = UNSET
        if not isinstance(self.grant_types_supported, Unset):
            grant_types_supported = self.grant_types_supported

        code_challenge_methods_supported: Union[Unset, list[str]] = UNSET
        if not isinstance(self.code_challenge_methods_supported, Unset):
            code_challenge_methods_supported = self.code_challenge_methods_supported

        audiences_supported: Union[Unset, list[str]] = UNSET
        if not isinstance(self.audiences_supported, Unset):
            audiences_supported = self.audiences_supported

        scopes_supported: Union[Unset, list[str]] = UNSET
        if not isinstance(self.scopes_supported, Unset):
            scopes_supported = self.scopes_supported

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if authorization_endpoint is not UNSET:
            field_dict["authorization_endpoint"] = authorization_endpoint
        if token_endpoint is not UNSET:
            field_dict["token_endpoint"] = token_endpoint
        if jwks_uri is not UNSET:
            field_dict["jwks_uri"] = jwks_uri
        if registration_endpoint is not UNSET:
            field_dict["registration_endpoint"] = registration_endpoint
        if revocation_endpoint is not UNSET:
            field_dict["revocation_endpoint"] = revocation_endpoint
        if token_exchange_endpoint is not UNSET:
            field_dict["token_exchange_endpoint"] = token_exchange_endpoint
        if response_types_supported is not UNSET:
            field_dict["response_types_supported"] = response_types_supported
        if grant_types_supported is not UNSET:
            field_dict["grant_types_supported"] = grant_types_supported
        if code_challenge_methods_supported is not UNSET:
            field_dict["code_challenge_methods_supported"] = code_challenge_methods_supported
        if audiences_supported is not UNSET:
            field_dict["audiences_supported"] = audiences_supported
        if scopes_supported is not UNSET:
            field_dict["scopes_supported"] = scopes_supported

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issuer = d.pop("issuer", UNSET)

        authorization_endpoint = d.pop("authorization_endpoint", UNSET)

        token_endpoint = d.pop("token_endpoint", UNSET)

        jwks_uri = d.pop("jwks_uri", UNSET)

        registration_endpoint = d.pop("registration_endpoint", UNSET)

        revocation_endpoint = d.pop("revocation_endpoint", UNSET)

        token_exchange_endpoint = d.pop("token_exchange_endpoint", UNSET)

        response_types_supported = cast(list[str], d.pop("response_types_supported", UNSET))

        grant_types_supported = cast(list[str], d.pop("grant_types_supported", UNSET))

        code_challenge_methods_supported = cast(list[str], d.pop("code_challenge_methods_supported", UNSET))

        audiences_supported = cast(list[str], d.pop("audiences_supported", UNSET))

        scopes_supported = cast(list[str], d.pop("scopes_supported", UNSET))

        oauth_2_metadata_response_200 = cls(
            issuer=issuer,
            authorization_endpoint=authorization_endpoint,
            token_endpoint=token_endpoint,
            jwks_uri=jwks_uri,
            registration_endpoint=registration_endpoint,
            revocation_endpoint=revocation_endpoint,
            token_exchange_endpoint=token_exchange_endpoint,
            response_types_supported=response_types_supported,
            grant_types_supported=grant_types_supported,
            code_challenge_methods_supported=code_challenge_methods_supported,
            audiences_supported=audiences_supported,
            scopes_supported=scopes_supported,
        )

        oauth_2_metadata_response_200.additional_properties = d
        return oauth_2_metadata_response_200

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
