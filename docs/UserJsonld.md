# UserJsonld



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**DefinitionJsonldEntityReadEntityReadParentContext**](DefinitionJsonldEntityReadEntityReadParentContext.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] 
**email** | **str** |  | 
**password** | **str** |  | [optional] 
**old_password** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**reset_password_link** | **str** |  | [optional] 
**activation_url** | **str** |  | [optional] 

## Example

```python
from jsonhub_sdk.models.user_jsonld import UserJsonld

# TODO update the JSON string below
json = "{}"
# create an instance of UserJsonld from a JSON string
user_jsonld_instance = UserJsonld.from_json(json)
# print the JSON string representation of the object
print(UserJsonld.to_json())

# convert the object into a dict
user_jsonld_dict = user_jsonld_instance.to_dict()
# create an instance of UserJsonld from a dict
user_jsonld_from_dict = UserJsonld.from_dict(user_jsonld_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


