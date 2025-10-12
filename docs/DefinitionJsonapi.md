# DefinitionJsonapi



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DefinitionJsonapiData**](DefinitionJsonapiData.md) |  | [optional] 
**parent_entity** | [**EntityJsonapi**](EntityJsonapi.md) |  | [optional] 
**is_owned_by_current_user** | **bool** |  | [optional] [readonly] 

## Example

```python
from jsonhub-sdk.models.definition_jsonapi import DefinitionJsonapi

# TODO update the JSON string below
json = "{}"
# create an instance of DefinitionJsonapi from a JSON string
definition_jsonapi_instance = DefinitionJsonapi.from_json(json)
# print the JSON string representation of the object
print(DefinitionJsonapi.to_json())

# convert the object into a dict
definition_jsonapi_dict = definition_jsonapi_instance.to_dict()
# create an instance of DefinitionJsonapi from a dict
definition_jsonapi_from_dict = DefinitionJsonapi.from_dict(definition_jsonapi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


