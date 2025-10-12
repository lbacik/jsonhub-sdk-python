# EntityJsonldEntityCreate



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**definition** | **str** |  | [optional] 
**parent** | [**EntityJsonldEntityCreate**](EntityJsonldEntityCreate.md) |  | [optional] 
**private** | **bool** |  | [optional] 

## Example

```python
from jsonhub_sdk.models.entity_jsonld_entity_create import EntityJsonldEntityCreate

# TODO update the JSON string below
json = "{}"
# create an instance of EntityJsonldEntityCreate from a JSON string
entity_jsonld_entity_create_instance = EntityJsonldEntityCreate.from_json(json)
# print the JSON string representation of the object
print(EntityJsonldEntityCreate.to_json())

# convert the object into a dict
entity_jsonld_entity_create_dict = entity_jsonld_entity_create_instance.to_dict()
# create an instance of EntityJsonldEntityCreate from a dict
entity_jsonld_entity_create_from_dict = EntityJsonldEntityCreate.from_dict(entity_jsonld_entity_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


