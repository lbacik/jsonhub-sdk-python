# DefinitionJsonhalDefinitionWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DefinitionJsonhalDefinitionReadLinks**](DefinitionJsonhalDefinitionReadLinks.md) |  | [optional] 
**slug** | **str** |  | [optional] 
**json_schema** | **object** |  | 
**parent_entity** | **str** |  | [optional] 

## Example

```python
from jsonhub-sdk.models.definition_jsonhal_definition_write import DefinitionJsonhalDefinitionWrite

# TODO update the JSON string below
json = "{}"
# create an instance of DefinitionJsonhalDefinitionWrite from a JSON string
definition_jsonhal_definition_write_instance = DefinitionJsonhalDefinitionWrite.from_json(json)
# print the JSON string representation of the object
print(DefinitionJsonhalDefinitionWrite.to_json())

# convert the object into a dict
definition_jsonhal_definition_write_dict = definition_jsonhal_definition_write_instance.to_dict()
# create an instance of DefinitionJsonhalDefinitionWrite from a dict
definition_jsonhal_definition_write_from_dict = DefinitionJsonhalDefinitionWrite.from_dict(definition_jsonhal_definition_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


