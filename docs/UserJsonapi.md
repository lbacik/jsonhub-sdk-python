# UserJsonapi



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserJsonapiData**](UserJsonapiData.md) |  | [optional] 

## Example

```python
from jsonhub_sdk.models.user_jsonapi import UserJsonapi

# TODO update the JSON string below
json = "{}"
# create an instance of UserJsonapi from a JSON string
user_jsonapi_instance = UserJsonapi.from_json(json)
# print the JSON string representation of the object
print(UserJsonapi.to_json())

# convert the object into a dict
user_jsonapi_dict = user_jsonapi_instance.to_dict()
# create an instance of UserJsonapi from a dict
user_jsonapi_from_dict = UserJsonapi.from_dict(user_jsonapi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


