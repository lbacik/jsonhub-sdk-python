# Oauth2JsonldOauth2Write



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_type** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from jsonhub_sdk.models.oauth2_jsonld_oauth2_write import Oauth2JsonldOauth2Write

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2JsonldOauth2Write from a JSON string
oauth2_jsonld_oauth2_write_instance = Oauth2JsonldOauth2Write.from_json(json)
# print the JSON string representation of the object
print(Oauth2JsonldOauth2Write.to_json())

# convert the object into a dict
oauth2_jsonld_oauth2_write_dict = oauth2_jsonld_oauth2_write_instance.to_dict()
# create an instance of Oauth2JsonldOauth2Write from a dict
oauth2_jsonld_oauth2_write_from_dict = Oauth2JsonldOauth2Write.from_dict(oauth2_jsonld_oauth2_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


