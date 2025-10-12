# DefinitionDefinitionRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**json_schema** | **object** |  | 
**parent_entity** | [**EntityDefinitionRead**](EntityDefinitionRead.md) |  | [optional] 
**is_owned_by_current_user** | **bool** |  | [optional] 

## Example

```python
from jsonhub_sdk.models.definition_definition_read import DefinitionDefinitionRead

# TODO update the JSON string below
json = "{}"
# create an instance of DefinitionDefinitionRead from a JSON string
definition_definition_read_instance = DefinitionDefinitionRead.from_json(json)
# print the JSON string representation of the object
print(DefinitionDefinitionRead.to_json())

# convert the object into a dict
definition_definition_read_dict = definition_definition_read_instance.to_dict()
# create an instance of DefinitionDefinitionRead from a dict
definition_definition_read_from_dict = DefinitionDefinitionRead.from_dict(definition_definition_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


