# Oauth2JsonhalOauth2Write



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DefinitionJsonhalDefinitionReadLinks**](DefinitionJsonhalDefinitionReadLinks.md) |  | [optional] 
**grant_type** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from jsonhub-sdk.models.oauth2_jsonhal_oauth2_write import Oauth2JsonhalOauth2Write

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2JsonhalOauth2Write from a JSON string
oauth2_jsonhal_oauth2_write_instance = Oauth2JsonhalOauth2Write.from_json(json)
# print the JSON string representation of the object
print(Oauth2JsonhalOauth2Write.to_json())

# convert the object into a dict
oauth2_jsonhal_oauth2_write_dict = oauth2_jsonhal_oauth2_write_instance.to_dict()
# create an instance of Oauth2JsonhalOauth2Write from a dict
oauth2_jsonhal_oauth2_write_from_dict = Oauth2JsonhalOauth2Write.from_dict(oauth2_jsonhal_oauth2_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


