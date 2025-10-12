# UserJsonhalUserSendResetPassword



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DefinitionJsonhalDefinitionReadLinks**](DefinitionJsonhalDefinitionReadLinks.md) |  | [optional] 
**email** | **str** |  | 
**reset_password_link** | **str** |  | 

## Example

```python
from jsonhub_sdk.models.user_jsonhal_user_send_reset_password import UserJsonhalUserSendResetPassword

# TODO update the JSON string below
json = "{}"
# create an instance of UserJsonhalUserSendResetPassword from a JSON string
user_jsonhal_user_send_reset_password_instance = UserJsonhalUserSendResetPassword.from_json(json)
# print the JSON string representation of the object
print(UserJsonhalUserSendResetPassword.to_json())

# convert the object into a dict
user_jsonhal_user_send_reset_password_dict = user_jsonhal_user_send_reset_password_instance.to_dict()
# create an instance of UserJsonhalUserSendResetPassword from a dict
user_jsonhal_user_send_reset_password_from_dict = UserJsonhalUserSendResetPassword.from_dict(user_jsonhal_user_send_reset_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


