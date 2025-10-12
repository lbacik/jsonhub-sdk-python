# UserUserResendActivation



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**activation_url** | **str** |  | [optional] 

## Example

```python
from jsonhub-sdk.models.user_user_resend_activation import UserUserResendActivation

# TODO update the JSON string below
json = "{}"
# create an instance of UserUserResendActivation from a JSON string
user_user_resend_activation_instance = UserUserResendActivation.from_json(json)
# print the JSON string representation of the object
print(UserUserResendActivation.to_json())

# convert the object into a dict
user_user_resend_activation_dict = user_user_resend_activation_instance.to_dict()
# create an instance of UserUserResendActivation from a dict
user_user_resend_activation_from_dict = UserUserResendActivation.from_dict(user_user_resend_activation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


