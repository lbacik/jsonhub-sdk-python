# EntityDefinitionRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 

## Example

```python
from jsonhub_sdk.models.entity_definition_read import EntityDefinitionRead

# TODO update the JSON string below
json = "{}"
# create an instance of EntityDefinitionRead from a JSON string
entity_definition_read_instance = EntityDefinitionRead.from_json(json)
# print the JSON string representation of the object
print(EntityDefinitionRead.to_json())

# convert the object into a dict
entity_definition_read_dict = entity_definition_read_instance.to_dict()
# create an instance of EntityDefinitionRead from a dict
entity_definition_read_from_dict = EntityDefinitionRead.from_dict(entity_definition_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


