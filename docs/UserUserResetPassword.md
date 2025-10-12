# UserUserResetPassword



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 
**token** | **str** |  | 

## Example

```python
from jsonhub_sdk.models.user_user_reset_password import UserUserResetPassword

# TODO update the JSON string below
json = "{}"
# create an instance of UserUserResetPassword from a JSON string
user_user_reset_password_instance = UserUserResetPassword.from_json(json)
# print the JSON string representation of the object
print(UserUserResetPassword.to_json())

# convert the object into a dict
user_user_reset_password_dict = user_user_reset_password_instance.to_dict()
# create an instance of UserUserResetPassword from a dict
user_user_reset_password_from_dict = UserUserResetPassword.from_dict(user_user_reset_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


