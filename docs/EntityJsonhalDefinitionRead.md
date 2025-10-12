# EntityJsonhalDefinitionRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DefinitionJsonhalDefinitionReadLinks**](DefinitionJsonhalDefinitionReadLinks.md) |  | [optional] 
**id** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 

## Example

```python
from jsonhub_sdk.models.entity_jsonhal_definition_read import EntityJsonhalDefinitionRead

# TODO update the JSON string below
json = "{}"
# create an instance of EntityJsonhalDefinitionRead from a JSON string
entity_jsonhal_definition_read_instance = EntityJsonhalDefinitionRead.from_json(json)
# print the JSON string representation of the object
print(EntityJsonhalDefinitionRead.to_json())

# convert the object into a dict
entity_jsonhal_definition_read_dict = entity_jsonhal_definition_read_instance.to_dict()
# create an instance of EntityJsonhalDefinitionRead from a dict
entity_jsonhal_definition_read_from_dict = EntityJsonhalDefinitionRead.from_dict(entity_jsonhal_definition_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


