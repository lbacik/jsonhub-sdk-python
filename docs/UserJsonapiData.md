# UserJsonapiData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**attributes** | [**UserJsonapiDataAttributes**](UserJsonapiDataAttributes.md) |  | [optional] 

## Example

```python
from jsonhub-sdk.models.user_jsonapi_data import UserJsonapiData

# TODO update the JSON string below
json = "{}"
# create an instance of UserJsonapiData from a JSON string
user_jsonapi_data_instance = UserJsonapiData.from_json(json)
# print the JSON string representation of the object
print(UserJsonapiData.to_json())

# convert the object into a dict
user_jsonapi_data_dict = user_jsonapi_data_instance.to_dict()
# create an instance of UserJsonapiData from a dict
user_jsonapi_data_from_dict = UserJsonapiData.from_dict(user_jsonapi_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


