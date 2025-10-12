# EntityJsonhalEntityReadEntityReadParent



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DefinitionJsonhalDefinitionReadLinks**](DefinitionJsonhalDefinitionReadLinks.md) |  | [optional] 
**id** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**definition** | [**DefinitionJsonhalEntityReadEntityReadParent**](DefinitionJsonhalEntityReadEntityReadParent.md) |  | [optional] 
**parent** | [**EntityJsonhalEntityReadEntityReadParent**](EntityJsonhalEntityReadEntityReadParent.md) |  | [optional] 
**private** | **bool** |  | [optional] 
**is_owned_by_current_user** | **bool** |  | [optional] 

## Example

```python
from jsonhub-sdk.models.entity_jsonhal_entity_read_entity_read_parent import EntityJsonhalEntityReadEntityReadParent

# TODO update the JSON string below
json = "{}"
# create an instance of EntityJsonhalEntityReadEntityReadParent from a JSON string
entity_jsonhal_entity_read_entity_read_parent_instance = EntityJsonhalEntityReadEntityReadParent.from_json(json)
# print the JSON string representation of the object
print(EntityJsonhalEntityReadEntityReadParent.to_json())

# convert the object into a dict
entity_jsonhal_entity_read_entity_read_parent_dict = entity_jsonhal_entity_read_entity_read_parent_instance.to_dict()
# create an instance of EntityJsonhalEntityReadEntityReadParent from a dict
entity_jsonhal_entity_read_entity_read_parent_from_dict = EntityJsonhalEntityReadEntityReadParent.from_dict(entity_jsonhal_entity_read_entity_read_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


