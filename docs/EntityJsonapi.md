# EntityJsonapi



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**slug** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**definition** | [**DefinitionJsonapi**](DefinitionJsonapi.md) |  | [optional] 
**parent** | [**EntityJsonapi**](EntityJsonapi.md) |  | [optional] 
**private** | **bool** |  | [optional] 
**is_owned_by_current_user** | **bool** |  | [optional] [readonly] 

## Example

```python
from jsonhub_sdk.models.entity_jsonapi import EntityJsonapi

# TODO update the JSON string below
json = "{}"
# create an instance of EntityJsonapi from a JSON string
entity_jsonapi_instance = EntityJsonapi.from_json(json)
# print the JSON string representation of the object
print(EntityJsonapi.to_json())

# convert the object into a dict
entity_jsonapi_dict = entity_jsonapi_instance.to_dict()
# create an instance of EntityJsonapi from a dict
entity_jsonapi_from_dict = EntityJsonapi.from_dict(entity_jsonapi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


