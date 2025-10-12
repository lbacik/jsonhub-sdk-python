# Oauth2JsonapiDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_type** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**access_token** | **str** |  | [optional] [readonly] 

## Example

```python
from jsonhub_sdk.models.oauth2_jsonapi_data_attributes import Oauth2JsonapiDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2JsonapiDataAttributes from a JSON string
oauth2_jsonapi_data_attributes_instance = Oauth2JsonapiDataAttributes.from_json(json)
# print the JSON string representation of the object
print(Oauth2JsonapiDataAttributes.to_json())

# convert the object into a dict
oauth2_jsonapi_data_attributes_dict = oauth2_jsonapi_data_attributes_instance.to_dict()
# create an instance of Oauth2JsonapiDataAttributes from a dict
oauth2_jsonapi_data_attributes_from_dict = Oauth2JsonapiDataAttributes.from_dict(oauth2_jsonapi_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


