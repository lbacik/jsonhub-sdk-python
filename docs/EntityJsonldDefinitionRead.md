# EntityJsonldDefinitionRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**DefinitionJsonldEntityReadEntityReadParentContext**](DefinitionJsonldEntityReadEntityReadParentContext.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 

## Example

```python
from jsonhub_sdk.models.entity_jsonld_definition_read import EntityJsonldDefinitionRead

# TODO update the JSON string below
json = "{}"
# create an instance of EntityJsonldDefinitionRead from a JSON string
entity_jsonld_definition_read_instance = EntityJsonldDefinitionRead.from_json(json)
# print the JSON string representation of the object
print(EntityJsonldDefinitionRead.to_json())

# convert the object into a dict
entity_jsonld_definition_read_dict = entity_jsonld_definition_read_instance.to_dict()
# create an instance of EntityJsonldDefinitionRead from a dict
entity_jsonld_definition_read_from_dict = EntityJsonldDefinitionRead.from_dict(entity_jsonld_definition_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


