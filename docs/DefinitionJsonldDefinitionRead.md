# DefinitionJsonldDefinitionRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**DefinitionJsonldDefinitionReadContext**](DefinitionJsonldDefinitionReadContext.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**json_schema** | **object** |  | 
**parent_entity** | [**EntityJsonldDefinitionRead**](EntityJsonldDefinitionRead.md) |  | [optional] 
**is_owned_by_current_user** | **bool** |  | [optional] 

## Example

```python
from jsonhub-sdk.models.definition_jsonld_definition_read import DefinitionJsonldDefinitionRead

# TODO update the JSON string below
json = "{}"
# create an instance of DefinitionJsonldDefinitionRead from a JSON string
definition_jsonld_definition_read_instance = DefinitionJsonldDefinitionRead.from_json(json)
# print the JSON string representation of the object
print(DefinitionJsonldDefinitionRead.to_json())

# convert the object into a dict
definition_jsonld_definition_read_dict = definition_jsonld_definition_read_instance.to_dict()
# create an instance of DefinitionJsonldDefinitionRead from a dict
definition_jsonld_definition_read_from_dict = DefinitionJsonldDefinitionRead.from_dict(definition_jsonld_definition_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


