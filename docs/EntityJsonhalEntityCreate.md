# EntityJsonhalEntityCreate



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DefinitionJsonhalDefinitionReadLinks**](DefinitionJsonhalDefinitionReadLinks.md) |  | [optional] 
**slug** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**definition** | **str** |  | [optional] 
**parent** | [**EntityJsonhalEntityCreate**](EntityJsonhalEntityCreate.md) |  | [optional] 
**private** | **bool** |  | [optional] 

## Example

```python
from jsonhub_sdk.models.entity_jsonhal_entity_create import EntityJsonhalEntityCreate

# TODO update the JSON string below
json = "{}"
# create an instance of EntityJsonhalEntityCreate from a JSON string
entity_jsonhal_entity_create_instance = EntityJsonhalEntityCreate.from_json(json)
# print the JSON string representation of the object
print(EntityJsonhalEntityCreate.to_json())

# convert the object into a dict
entity_jsonhal_entity_create_dict = entity_jsonhal_entity_create_instance.to_dict()
# create an instance of EntityJsonhalEntityCreate from a dict
entity_jsonhal_entity_create_from_dict = EntityJsonhalEntityCreate.from_dict(entity_jsonhal_entity_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


