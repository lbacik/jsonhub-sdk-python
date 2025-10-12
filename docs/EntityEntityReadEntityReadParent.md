# EntityEntityReadEntityReadParent



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**definition** | [**DefinitionEntityReadEntityReadParent**](DefinitionEntityReadEntityReadParent.md) |  | [optional] 
**parent** | [**EntityEntityReadEntityReadParent**](EntityEntityReadEntityReadParent.md) |  | [optional] 
**private** | **bool** |  | [optional] 
**is_owned_by_current_user** | **bool** |  | [optional] 

## Example

```python
from jsonhub-sdk.models.entity_entity_read_entity_read_parent import EntityEntityReadEntityReadParent

# TODO update the JSON string below
json = "{}"
# create an instance of EntityEntityReadEntityReadParent from a JSON string
entity_entity_read_entity_read_parent_instance = EntityEntityReadEntityReadParent.from_json(json)
# print the JSON string representation of the object
print(EntityEntityReadEntityReadParent.to_json())

# convert the object into a dict
entity_entity_read_entity_read_parent_dict = entity_entity_read_entity_read_parent_instance.to_dict()
# create an instance of EntityEntityReadEntityReadParent from a dict
entity_entity_read_entity_read_parent_from_dict = EntityEntityReadEntityReadParent.from_dict(entity_entity_read_entity_read_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


