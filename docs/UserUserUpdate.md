# UserUserUpdate

Change user password

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 
**old_password** | **str** |  | [optional] 

## Example

```python
from jsonhub_sdk.models.user_user_update import UserUserUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UserUserUpdate from a JSON string
user_user_update_instance = UserUserUpdate.from_json(json)
# print the JSON string representation of the object
print(UserUserUpdate.to_json())

# convert the object into a dict
user_user_update_dict = user_user_update_instance.to_dict()
# create an instance of UserUserUpdate from a dict
user_user_update_from_dict = UserUserUpdate.from_dict(user_user_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


