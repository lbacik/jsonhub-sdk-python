# UserJsonhalUserEmpty

Change user password

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DefinitionJsonhalDefinitionReadLinks**](DefinitionJsonhalDefinitionReadLinks.md) |  | [optional] 

## Example

```python
from jsonhub_sdk.models.user_jsonhal_user_empty import UserJsonhalUserEmpty

# TODO update the JSON string below
json = "{}"
# create an instance of UserJsonhalUserEmpty from a JSON string
user_jsonhal_user_empty_instance = UserJsonhalUserEmpty.from_json(json)
# print the JSON string representation of the object
print(UserJsonhalUserEmpty.to_json())

# convert the object into a dict
user_jsonhal_user_empty_dict = user_jsonhal_user_empty_instance.to_dict()
# create an instance of UserJsonhalUserEmpty from a dict
user_jsonhal_user_empty_from_dict = UserJsonhalUserEmpty.from_dict(user_jsonhal_user_empty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


