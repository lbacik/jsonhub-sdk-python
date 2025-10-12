# Oauth2JsonhalOauth2Read



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DefinitionJsonhalDefinitionReadLinks**](DefinitionJsonhalDefinitionReadLinks.md) |  | [optional] 
**access_token** | **str** |  | [optional] 

## Example

```python
from jsonhub-sdk.models.oauth2_jsonhal_oauth2_read import Oauth2JsonhalOauth2Read

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2JsonhalOauth2Read from a JSON string
oauth2_jsonhal_oauth2_read_instance = Oauth2JsonhalOauth2Read.from_json(json)
# print the JSON string representation of the object
print(Oauth2JsonhalOauth2Read.to_json())

# convert the object into a dict
oauth2_jsonhal_oauth2_read_dict = oauth2_jsonhal_oauth2_read_instance.to_dict()
# create an instance of Oauth2JsonhalOauth2Read from a dict
oauth2_jsonhal_oauth2_read_from_dict = Oauth2JsonhalOauth2Read.from_dict(oauth2_jsonhal_oauth2_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


