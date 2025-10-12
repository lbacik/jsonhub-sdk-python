# DefinitionJsonhalDefinitionRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DefinitionJsonhalDefinitionReadLinks**](DefinitionJsonhalDefinitionReadLinks.md) |  | [optional] 
**id** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**json_schema** | **object** |  | 
**parent_entity** | [**EntityJsonhalDefinitionRead**](EntityJsonhalDefinitionRead.md) |  | [optional] 
**is_owned_by_current_user** | **bool** |  | [optional] 

## Example

```python
from jsonhub-sdk.models.definition_jsonhal_definition_read import DefinitionJsonhalDefinitionRead

# TODO update the JSON string below
json = "{}"
# create an instance of DefinitionJsonhalDefinitionRead from a JSON string
definition_jsonhal_definition_read_instance = DefinitionJsonhalDefinitionRead.from_json(json)
# print the JSON string representation of the object
print(DefinitionJsonhalDefinitionRead.to_json())

# convert the object into a dict
definition_jsonhal_definition_read_dict = definition_jsonhal_definition_read_instance.to_dict()
# create an instance of DefinitionJsonhalDefinitionRead from a dict
definition_jsonhal_definition_read_from_dict = DefinitionJsonhalDefinitionRead.from_dict(definition_jsonhal_definition_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


