# Oauth2JsonapiData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**attributes** | [**Oauth2JsonapiDataAttributes**](Oauth2JsonapiDataAttributes.md) |  | [optional] 

## Example

```python
from jsonhub-sdk.models.oauth2_jsonapi_data import Oauth2JsonapiData

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2JsonapiData from a JSON string
oauth2_jsonapi_data_instance = Oauth2JsonapiData.from_json(json)
# print the JSON string representation of the object
print(Oauth2JsonapiData.to_json())

# convert the object into a dict
oauth2_jsonapi_data_dict = oauth2_jsonapi_data_instance.to_dict()
# create an instance of Oauth2JsonapiData from a dict
oauth2_jsonapi_data_from_dict = Oauth2JsonapiData.from_dict(oauth2_jsonapi_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


