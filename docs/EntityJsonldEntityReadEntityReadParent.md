# EntityJsonldEntityReadEntityReadParent



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**DefinitionJsonldEntityReadEntityReadParentContext**](DefinitionJsonldEntityReadEntityReadParentContext.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**definition** | [**DefinitionJsonldEntityReadEntityReadParent**](DefinitionJsonldEntityReadEntityReadParent.md) |  | [optional] 
**parent** | [**EntityJsonldEntityReadEntityReadParent**](EntityJsonldEntityReadEntityReadParent.md) |  | [optional] 
**private** | **bool** |  | [optional] 
**is_owned_by_current_user** | **bool** |  | [optional] 

## Example

```python
from jsonhub-sdk.models.entity_jsonld_entity_read_entity_read_parent import EntityJsonldEntityReadEntityReadParent

# TODO update the JSON string below
json = "{}"
# create an instance of EntityJsonldEntityReadEntityReadParent from a JSON string
entity_jsonld_entity_read_entity_read_parent_instance = EntityJsonldEntityReadEntityReadParent.from_json(json)
# print the JSON string representation of the object
print(EntityJsonldEntityReadEntityReadParent.to_json())

# convert the object into a dict
entity_jsonld_entity_read_entity_read_parent_dict = entity_jsonld_entity_read_entity_read_parent_instance.to_dict()
# create an instance of EntityJsonldEntityReadEntityReadParent from a dict
entity_jsonld_entity_read_entity_read_parent_from_dict = EntityJsonldEntityReadEntityReadParent.from_dict(entity_jsonld_entity_read_entity_read_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


