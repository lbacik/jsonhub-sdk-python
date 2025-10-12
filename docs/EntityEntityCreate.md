# EntityEntityCreate



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**definition** | **str** |  | [optional] 
**parent** | [**EntityEntityCreate**](EntityEntityCreate.md) |  | [optional] 
**private** | **bool** |  | [optional] 

## Example

```python
from jsonhub-sdk.models.entity_entity_create import EntityEntityCreate

# TODO update the JSON string below
json = "{}"
# create an instance of EntityEntityCreate from a JSON string
entity_entity_create_instance = EntityEntityCreate.from_json(json)
# print the JSON string representation of the object
print(EntityEntityCreate.to_json())

# convert the object into a dict
entity_entity_create_dict = entity_entity_create_instance.to_dict()
# create an instance of EntityEntityCreate from a dict
entity_entity_create_from_dict = EntityEntityCreate.from_dict(entity_entity_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


