# UserJsonhalUserRead

Create user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DefinitionJsonhalDefinitionReadLinks**](DefinitionJsonhalDefinitionReadLinks.md) |  | [optional] 
**id** | **str** |  | [optional] 
**email** | **str** |  | 

## Example

```python
from jsonhub_sdk.models.user_jsonhal_user_read import UserJsonhalUserRead

# TODO update the JSON string below
json = "{}"
# create an instance of UserJsonhalUserRead from a JSON string
user_jsonhal_user_read_instance = UserJsonhalUserRead.from_json(json)
# print the JSON string representation of the object
print(UserJsonhalUserRead.to_json())

# convert the object into a dict
user_jsonhal_user_read_dict = user_jsonhal_user_read_instance.to_dict()
# create an instance of UserJsonhalUserRead from a dict
user_jsonhal_user_read_from_dict = UserJsonhalUserRead.from_dict(user_jsonhal_user_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


