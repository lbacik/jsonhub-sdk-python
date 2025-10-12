# DefinitionJsonapiData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**attributes** | [**DefinitionJsonapiDataAttributes**](DefinitionJsonapiDataAttributes.md) |  | [optional] 

## Example

```python
from jsonhub-sdk.models.definition_jsonapi_data import DefinitionJsonapiData

# TODO update the JSON string below
json = "{}"
# create an instance of DefinitionJsonapiData from a JSON string
definition_jsonapi_data_instance = DefinitionJsonapiData.from_json(json)
# print the JSON string representation of the object
print(DefinitionJsonapiData.to_json())

# convert the object into a dict
definition_jsonapi_data_dict = definition_jsonapi_data_instance.to_dict()
# create an instance of DefinitionJsonapiData from a dict
definition_jsonapi_data_from_dict = DefinitionJsonapiData.from_dict(definition_jsonapi_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


