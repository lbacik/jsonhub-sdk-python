# UserJsonhalUserResetPassword



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DefinitionJsonhalDefinitionReadLinks**](DefinitionJsonhalDefinitionReadLinks.md) |  | [optional] 
**password** | **str** |  | 
**token** | **str** |  | 

## Example

```python
from jsonhub_sdk.models.user_jsonhal_user_reset_password import UserJsonhalUserResetPassword

# TODO update the JSON string below
json = "{}"
# create an instance of UserJsonhalUserResetPassword from a JSON string
user_jsonhal_user_reset_password_instance = UserJsonhalUserResetPassword.from_json(json)
# print the JSON string representation of the object
print(UserJsonhalUserResetPassword.to_json())

# convert the object into a dict
user_jsonhal_user_reset_password_dict = user_jsonhal_user_reset_password_instance.to_dict()
# create an instance of UserJsonhalUserResetPassword from a dict
user_jsonhal_user_reset_password_from_dict = UserJsonhalUserResetPassword.from_dict(user_jsonhal_user_reset_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


