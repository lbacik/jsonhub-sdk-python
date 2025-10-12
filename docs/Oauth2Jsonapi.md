# Oauth2Jsonapi



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Oauth2JsonapiData**](Oauth2JsonapiData.md) |  | [optional] 

## Example

```python
from jsonhub_sdk.models.oauth2_jsonapi import Oauth2Jsonapi

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2Jsonapi from a JSON string
oauth2_jsonapi_instance = Oauth2Jsonapi.from_json(json)
# print the JSON string representation of the object
print(Oauth2Jsonapi.to_json())

# convert the object into a dict
oauth2_jsonapi_dict = oauth2_jsonapi_instance.to_dict()
# create an instance of Oauth2Jsonapi from a dict
oauth2_jsonapi_from_dict = Oauth2Jsonapi.from_dict(oauth2_jsonapi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


