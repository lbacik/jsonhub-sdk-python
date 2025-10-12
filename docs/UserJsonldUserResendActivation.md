# UserJsonldUserResendActivation



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**activation_url** | **str** |  | [optional] 

## Example

```python
from jsonhub_sdk.models.user_jsonld_user_resend_activation import UserJsonldUserResendActivation

# TODO update the JSON string below
json = "{}"
# create an instance of UserJsonldUserResendActivation from a JSON string
user_jsonld_user_resend_activation_instance = UserJsonldUserResendActivation.from_json(json)
# print the JSON string representation of the object
print(UserJsonldUserResendActivation.to_json())

# convert the object into a dict
user_jsonld_user_resend_activation_dict = user_jsonld_user_resend_activation_instance.to_dict()
# create an instance of UserJsonldUserResendActivation from a dict
user_jsonld_user_resend_activation_from_dict = UserJsonldUserResendActivation.from_dict(user_jsonld_user_resend_activation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


