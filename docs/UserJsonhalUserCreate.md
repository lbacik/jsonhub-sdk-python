# UserJsonhalUserCreate

Create user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DefinitionJsonhalDefinitionReadLinks**](DefinitionJsonhalDefinitionReadLinks.md) |  | [optional] 
**email** | **str** |  | 
**password** | **str** |  | 
**activation_url** | **str** |  | [optional] 

## Example

```python
from jsonhub-sdk.models.user_jsonhal_user_create import UserJsonhalUserCreate

# TODO update the JSON string below
json = "{}"
# create an instance of UserJsonhalUserCreate from a JSON string
user_jsonhal_user_create_instance = UserJsonhalUserCreate.from_json(json)
# print the JSON string representation of the object
print(UserJsonhalUserCreate.to_json())

# convert the object into a dict
user_jsonhal_user_create_dict = user_jsonhal_user_create_instance.to_dict()
# create an instance of UserJsonhalUserCreate from a dict
user_jsonhal_user_create_from_dict = UserJsonhalUserCreate.from_dict(user_jsonhal_user_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


