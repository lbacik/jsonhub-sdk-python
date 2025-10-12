# ApiDefinitionsGetCollection200ResponseLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**ApiDefinitionsGetCollection200ResponseLinksSelf**](ApiDefinitionsGetCollection200ResponseLinksSelf.md) |  | [optional] 
**first** | [**ApiDefinitionsGetCollection200ResponseLinksSelf**](ApiDefinitionsGetCollection200ResponseLinksSelf.md) |  | [optional] 
**last** | [**ApiDefinitionsGetCollection200ResponseLinksSelf**](ApiDefinitionsGetCollection200ResponseLinksSelf.md) |  | [optional] 
**next** | [**ApiDefinitionsGetCollection200ResponseLinksSelf**](ApiDefinitionsGetCollection200ResponseLinksSelf.md) |  | [optional] 
**previous** | [**ApiDefinitionsGetCollection200ResponseLinksSelf**](ApiDefinitionsGetCollection200ResponseLinksSelf.md) |  | [optional] 

## Example

```python
from jsonhub-sdk.models.api_definitions_get_collection200_response_links import ApiDefinitionsGetCollection200ResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDefinitionsGetCollection200ResponseLinks from a JSON string
api_definitions_get_collection200_response_links_instance = ApiDefinitionsGetCollection200ResponseLinks.from_json(json)
# print the JSON string representation of the object
print(ApiDefinitionsGetCollection200ResponseLinks.to_json())

# convert the object into a dict
api_definitions_get_collection200_response_links_dict = api_definitions_get_collection200_response_links_instance.to_dict()
# create an instance of ApiDefinitionsGetCollection200ResponseLinks from a dict
api_definitions_get_collection200_response_links_from_dict = ApiDefinitionsGetCollection200ResponseLinks.from_dict(api_definitions_get_collection200_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


