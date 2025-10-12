# DefinitionDefinitionWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**json_schema** | **object** |  | 
**parent_entity** | **str** |  | [optional] 

## Example

```python
from jsonhub_sdk.models.definition_definition_write import DefinitionDefinitionWrite

# TODO update the JSON string below
json = "{}"
# create an instance of DefinitionDefinitionWrite from a JSON string
definition_definition_write_instance = DefinitionDefinitionWrite.from_json(json)
# print the JSON string representation of the object
print(DefinitionDefinitionWrite.to_json())

# convert the object into a dict
definition_definition_write_dict = definition_definition_write_instance.to_dict()
# create an instance of DefinitionDefinitionWrite from a dict
definition_definition_write_from_dict = DefinitionDefinitionWrite.from_dict(definition_definition_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


