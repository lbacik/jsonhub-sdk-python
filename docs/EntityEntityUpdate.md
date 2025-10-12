# EntityEntityUpdate



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**parent** | [**EntityEntityUpdate**](EntityEntityUpdate.md) |  | [optional] 
**private** | **bool** |  | [optional] 

## Example

```python
from jsonhub_sdk.models.entity_entity_update import EntityEntityUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of EntityEntityUpdate from a JSON string
entity_entity_update_instance = EntityEntityUpdate.from_json(json)
# print the JSON string representation of the object
print(EntityEntityUpdate.to_json())

# convert the object into a dict
entity_entity_update_dict = entity_entity_update_instance.to_dict()
# create an instance of EntityEntityUpdate from a dict
entity_entity_update_from_dict = EntityEntityUpdate.from_dict(entity_entity_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


