# ApiDefinitionsGetCollection200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**ApiDefinitionsGetCollection200ResponseEmbedded**](ApiDefinitionsGetCollection200ResponseEmbedded.md) |  | 
**total_items** | **int** |  | [optional] 
**items_per_page** | **int** |  | [optional] 
**links** | [**ApiDefinitionsGetCollection200ResponseLinks**](ApiDefinitionsGetCollection200ResponseLinks.md) |  | 

## Example

```python
from jsonhub_sdk.models.api_definitions_get_collection200_response import ApiDefinitionsGetCollection200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDefinitionsGetCollection200Response from a JSON string
api_definitions_get_collection200_response_instance = ApiDefinitionsGetCollection200Response.from_json(json)
# print the JSON string representation of the object
print(ApiDefinitionsGetCollection200Response.to_json())

# convert the object into a dict
api_definitions_get_collection200_response_dict = api_definitions_get_collection200_response_instance.to_dict()
# create an instance of ApiDefinitionsGetCollection200Response from a dict
api_definitions_get_collection200_response_from_dict = ApiDefinitionsGetCollection200Response.from_dict(api_definitions_get_collection200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


