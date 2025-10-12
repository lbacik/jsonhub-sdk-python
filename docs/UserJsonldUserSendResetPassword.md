# UserJsonldUserSendResetPassword



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**reset_password_link** | **str** |  | 

## Example

```python
from jsonhub_sdk.models.user_jsonld_user_send_reset_password import UserJsonldUserSendResetPassword

# TODO update the JSON string below
json = "{}"
# create an instance of UserJsonldUserSendResetPassword from a JSON string
user_jsonld_user_send_reset_password_instance = UserJsonldUserSendResetPassword.from_json(json)
# print the JSON string representation of the object
print(UserJsonldUserSendResetPassword.to_json())

# convert the object into a dict
user_jsonld_user_send_reset_password_dict = user_jsonld_user_send_reset_password_instance.to_dict()
# create an instance of UserJsonldUserSendResetPassword from a dict
user_jsonld_user_send_reset_password_from_dict = UserJsonldUserSendResetPassword.from_dict(user_jsonld_user_send_reset_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


