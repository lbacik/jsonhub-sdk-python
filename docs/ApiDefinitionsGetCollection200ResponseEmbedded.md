# ApiDefinitionsGetCollection200ResponseEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**List[DefinitionJsonhalDefinitionRead]**](DefinitionJsonhalDefinitionRead.md) |  | [optional] 

## Example

```python
from jsonhub-sdk.models.api_definitions_get_collection200_response_embedded import ApiDefinitionsGetCollection200ResponseEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDefinitionsGetCollection200ResponseEmbedded from a JSON string
api_definitions_get_collection200_response_embedded_instance = ApiDefinitionsGetCollection200ResponseEmbedded.from_json(json)
# print the JSON string representation of the object
print(ApiDefinitionsGetCollection200ResponseEmbedded.to_json())

# convert the object into a dict
api_definitions_get_collection200_response_embedded_dict = api_definitions_get_collection200_response_embedded_instance.to_dict()
# create an instance of ApiDefinitionsGetCollection200ResponseEmbedded from a dict
api_definitions_get_collection200_response_embedded_from_dict = ApiDefinitionsGetCollection200ResponseEmbedded.from_dict(api_definitions_get_collection200_response_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


