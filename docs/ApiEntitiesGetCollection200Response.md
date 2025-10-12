# ApiEntitiesGetCollection200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**ApiEntitiesGetCollection200ResponseEmbedded**](ApiEntitiesGetCollection200ResponseEmbedded.md) |  | 
**total_items** | **int** |  | [optional] 
**items_per_page** | **int** |  | [optional] 
**links** | [**ApiDefinitionsGetCollection200ResponseLinks**](ApiDefinitionsGetCollection200ResponseLinks.md) |  | 

## Example

```python
from jsonhub-sdk.models.api_entities_get_collection200_response import ApiEntitiesGetCollection200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiEntitiesGetCollection200Response from a JSON string
api_entities_get_collection200_response_instance = ApiEntitiesGetCollection200Response.from_json(json)
# print the JSON string representation of the object
print(ApiEntitiesGetCollection200Response.to_json())

# convert the object into a dict
api_entities_get_collection200_response_dict = api_entities_get_collection200_response_instance.to_dict()
# create an instance of ApiEntitiesGetCollection200Response from a dict
api_entities_get_collection200_response_from_dict = ApiEntitiesGetCollection200Response.from_dict(api_entities_get_collection200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


