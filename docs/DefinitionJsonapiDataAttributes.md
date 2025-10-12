# DefinitionJsonapiDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**slug** | **str** |  | [optional] 
**json_schema** | **object** |  | 

## Example

```python
from jsonhub-sdk.models.definition_jsonapi_data_attributes import DefinitionJsonapiDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DefinitionJsonapiDataAttributes from a JSON string
definition_jsonapi_data_attributes_instance = DefinitionJsonapiDataAttributes.from_json(json)
# print the JSON string representation of the object
print(DefinitionJsonapiDataAttributes.to_json())

# convert the object into a dict
definition_jsonapi_data_attributes_dict = definition_jsonapi_data_attributes_instance.to_dict()
# create an instance of DefinitionJsonapiDataAttributes from a dict
definition_jsonapi_data_attributes_from_dict = DefinitionJsonapiDataAttributes.from_dict(definition_jsonapi_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


