# DefinitionJsonldDefinitionWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**json_schema** | **object** |  | 
**parent_entity** | **str** |  | [optional] 

## Example

```python
from jsonhub-sdk.models.definition_jsonld_definition_write import DefinitionJsonldDefinitionWrite

# TODO update the JSON string below
json = "{}"
# create an instance of DefinitionJsonldDefinitionWrite from a JSON string
definition_jsonld_definition_write_instance = DefinitionJsonldDefinitionWrite.from_json(json)
# print the JSON string representation of the object
print(DefinitionJsonldDefinitionWrite.to_json())

# convert the object into a dict
definition_jsonld_definition_write_dict = definition_jsonld_definition_write_instance.to_dict()
# create an instance of DefinitionJsonldDefinitionWrite from a dict
definition_jsonld_definition_write_from_dict = DefinitionJsonldDefinitionWrite.from_dict(definition_jsonld_definition_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


