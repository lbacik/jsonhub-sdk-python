# UserJsonhalUserResendActivation



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DefinitionJsonhalDefinitionReadLinks**](DefinitionJsonhalDefinitionReadLinks.md) |  | [optional] 
**email** | **str** |  | 
**activation_url** | **str** |  | [optional] 

## Example

```python
from jsonhub-sdk.models.user_jsonhal_user_resend_activation import UserJsonhalUserResendActivation

# TODO update the JSON string below
json = "{}"
# create an instance of UserJsonhalUserResendActivation from a JSON string
user_jsonhal_user_resend_activation_instance = UserJsonhalUserResendActivation.from_json(json)
# print the JSON string representation of the object
print(UserJsonhalUserResendActivation.to_json())

# convert the object into a dict
user_jsonhal_user_resend_activation_dict = user_jsonhal_user_resend_activation_instance.to_dict()
# create an instance of UserJsonhalUserResendActivation from a dict
user_jsonhal_user_resend_activation_from_dict = UserJsonhalUserResendActivation.from_dict(user_jsonhal_user_resend_activation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


