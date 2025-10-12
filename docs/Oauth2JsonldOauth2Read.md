# Oauth2JsonldOauth2Read



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**DefinitionJsonldEntityReadEntityReadParentContext**](DefinitionJsonldEntityReadEntityReadParentContext.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**access_token** | **str** |  | [optional] 

## Example

```python
from jsonhub_sdk.models.oauth2_jsonld_oauth2_read import Oauth2JsonldOauth2Read

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2JsonldOauth2Read from a JSON string
oauth2_jsonld_oauth2_read_instance = Oauth2JsonldOauth2Read.from_json(json)
# print the JSON string representation of the object
print(Oauth2JsonldOauth2Read.to_json())

# convert the object into a dict
oauth2_jsonld_oauth2_read_dict = oauth2_jsonld_oauth2_read_instance.to_dict()
# create an instance of Oauth2JsonldOauth2Read from a dict
oauth2_jsonld_oauth2_read_from_dict = Oauth2JsonldOauth2Read.from_dict(oauth2_jsonld_oauth2_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


