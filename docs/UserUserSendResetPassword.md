# UserUserSendResetPassword



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**reset_password_link** | **str** |  | 

## Example

```python
from jsonhub_sdk.models.user_user_send_reset_password import UserUserSendResetPassword

# TODO update the JSON string below
json = "{}"
# create an instance of UserUserSendResetPassword from a JSON string
user_user_send_reset_password_instance = UserUserSendResetPassword.from_json(json)
# print the JSON string representation of the object
print(UserUserSendResetPassword.to_json())

# convert the object into a dict
user_user_send_reset_password_dict = user_user_send_reset_password_instance.to_dict()
# create an instance of UserUserSendResetPassword from a dict
user_user_send_reset_password_from_dict = UserUserSendResetPassword.from_dict(user_user_send_reset_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


