# UserJsonldUserEmpty

Change user password

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**DefinitionJsonldEntityReadEntityReadParentContext**](DefinitionJsonldEntityReadEntityReadParentContext.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 

## Example

```python
from jsonhub_sdk.models.user_jsonld_user_empty import UserJsonldUserEmpty

# TODO update the JSON string below
json = "{}"
# create an instance of UserJsonldUserEmpty from a JSON string
user_jsonld_user_empty_instance = UserJsonldUserEmpty.from_json(json)
# print the JSON string representation of the object
print(UserJsonldUserEmpty.to_json())

# convert the object into a dict
user_jsonld_user_empty_dict = user_jsonld_user_empty_instance.to_dict()
# create an instance of UserJsonldUserEmpty from a dict
user_jsonld_user_empty_from_dict = UserJsonldUserEmpty.from_dict(user_jsonld_user_empty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


