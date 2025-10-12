# UserUserCreate

Create user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 
**activation_url** | **str** |  | [optional] 

## Example

```python
from jsonhub_sdk.models.user_user_create import UserUserCreate

# TODO update the JSON string below
json = "{}"
# create an instance of UserUserCreate from a JSON string
user_user_create_instance = UserUserCreate.from_json(json)
# print the JSON string representation of the object
print(UserUserCreate.to_json())

# convert the object into a dict
user_user_create_dict = user_user_create_instance.to_dict()
# create an instance of UserUserCreate from a dict
user_user_create_from_dict = UserUserCreate.from_dict(user_user_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


