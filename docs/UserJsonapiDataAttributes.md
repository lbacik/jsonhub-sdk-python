# UserJsonapiDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | 
**password** | **str** |  | [optional] 
**old_password** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**reset_password_link** | **str** |  | [optional] 
**activation_url** | **str** |  | [optional] 

## Example

```python
from jsonhub_sdk.models.user_jsonapi_data_attributes import UserJsonapiDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserJsonapiDataAttributes from a JSON string
user_jsonapi_data_attributes_instance = UserJsonapiDataAttributes.from_json(json)
# print the JSON string representation of the object
print(UserJsonapiDataAttributes.to_json())

# convert the object into a dict
user_jsonapi_data_attributes_dict = user_jsonapi_data_attributes_instance.to_dict()
# create an instance of UserJsonapiDataAttributes from a dict
user_jsonapi_data_attributes_from_dict = UserJsonapiDataAttributes.from_dict(user_jsonapi_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


