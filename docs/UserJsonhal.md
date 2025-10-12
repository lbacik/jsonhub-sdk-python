# UserJsonhal



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DefinitionJsonhalDefinitionReadLinks**](DefinitionJsonhalDefinitionReadLinks.md) |  | [optional] 
**id** | **str** |  | [optional] 
**email** | **str** |  | 
**password** | **str** |  | [optional] 
**old_password** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**reset_password_link** | **str** |  | [optional] 
**activation_url** | **str** |  | [optional] 

## Example

```python
from jsonhub-sdk.models.user_jsonhal import UserJsonhal

# TODO update the JSON string below
json = "{}"
# create an instance of UserJsonhal from a JSON string
user_jsonhal_instance = UserJsonhal.from_json(json)
# print the JSON string representation of the object
print(UserJsonhal.to_json())

# convert the object into a dict
user_jsonhal_dict = user_jsonhal_instance.to_dict()
# create an instance of UserJsonhal from a dict
user_jsonhal_from_dict = UserJsonhal.from_dict(user_jsonhal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


