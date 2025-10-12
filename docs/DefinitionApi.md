# jsonhub_sdk.DefinitionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_definitions_get_collection**](DefinitionApi.md#api_definitions_get_collection) | **GET** /api/definitions | Retrieves the collection of definition resources.
[**api_definitions_id_delete**](DefinitionApi.md#api_definitions_id_delete) | **DELETE** /api/definitions/{id} | Removes the definition resource.
[**api_definitions_id_get**](DefinitionApi.md#api_definitions_id_get) | **GET** /api/definitions/{id} | Retrieves a definition resource.
[**api_definitions_id_patch**](DefinitionApi.md#api_definitions_id_patch) | **PATCH** /api/definitions/{id} | Updates the definition resource.
[**api_definitions_post**](DefinitionApi.md#api_definitions_post) | **POST** /api/definitions | Creates a definition resource.


# **api_definitions_get_collection**
> ApiDefinitionsGetCollection200Response api_definitions_get_collection(qid=qid, owned=owned, page=page, limit=limit, properties=properties, parent_entity=parent_entity)

Retrieves the collection of definition resources.

Retrieves the collection of definition resources.

### Example

* Bearer Authentication (access_token):

```python
import jsonhub_sdk
from jsonhub_sdk.models.api_definitions_get_collection200_response import ApiDefinitionsGetCollection200Response
from jsonhub_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jsonhub_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = jsonhub_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jsonhub_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jsonhub_sdk.DefinitionApi(api_client)
    qid = 'qid_example' # str | Filter by slug/id (partial match) (optional)
    owned = True # bool | Show only definitions owned by the current user (optional)
    page = 1 # int | The collection page number (optional) (default to 1)
    limit = 10 # int | The number of items per page (optional) (default to 10)
    properties = ['properties_example'] # List[str] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty} (optional)
    parent_entity = 'parent_entity_example' # str | Filter by parentEntity (uuid) (optional)

    try:
        # Retrieves the collection of definition resources.
        api_response = api_instance.api_definitions_get_collection(qid=qid, owned=owned, page=page, limit=limit, properties=properties, parent_entity=parent_entity)
        print("The response of DefinitionApi->api_definitions_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefinitionApi->api_definitions_get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qid** | **str**| Filter by slug/id (partial match) | [optional] 
 **owned** | **bool**| Show only definitions owned by the current user | [optional] 
 **page** | **int**| The collection page number | [optional] [default to 1]
 **limit** | **int**| The number of items per page | [optional] [default to 10]
 **properties** | [**List[str]**](str.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] 
 **parent_entity** | **str**| Filter by parentEntity (uuid) | [optional] 

### Return type

[**ApiDefinitionsGetCollection200Response**](ApiDefinitionsGetCollection200Response.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | definition collection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_definitions_id_delete**
> api_definitions_id_delete(id)

Removes the definition resource.

Removes the definition resource.

### Example

* Bearer Authentication (access_token):

```python
import jsonhub_sdk
from jsonhub_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jsonhub_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = jsonhub_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jsonhub_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jsonhub_sdk.DefinitionApi(api_client)
    id = 'id_example' # str | definition identifier

    try:
        # Removes the definition resource.
        api_instance.api_definitions_id_delete(id)
    except Exception as e:
        print("Exception when calling DefinitionApi->api_definitions_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| definition identifier | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | definition resource deleted |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_definitions_id_get**
> DefinitionJsonhalDefinitionRead api_definitions_id_get(id)

Retrieves a definition resource.

Retrieves a definition resource.

### Example

* Bearer Authentication (access_token):

```python
import jsonhub_sdk
from jsonhub_sdk.models.definition_jsonhal_definition_read import DefinitionJsonhalDefinitionRead
from jsonhub_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jsonhub_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = jsonhub_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jsonhub_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jsonhub_sdk.DefinitionApi(api_client)
    id = 'id_example' # str | definition identifier

    try:
        # Retrieves a definition resource.
        api_response = api_instance.api_definitions_id_get(id)
        print("The response of DefinitionApi->api_definitions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefinitionApi->api_definitions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| definition identifier | 

### Return type

[**DefinitionJsonhalDefinitionRead**](DefinitionJsonhalDefinitionRead.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | definition resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_definitions_id_patch**
> DefinitionJsonhalDefinitionRead api_definitions_id_patch(id, definition_definition_write)

Updates the definition resource.

Updates the definition resource.

### Example

* Bearer Authentication (access_token):

```python
import jsonhub_sdk
from jsonhub_sdk.models.definition_definition_write import DefinitionDefinitionWrite
from jsonhub_sdk.models.definition_jsonhal_definition_read import DefinitionJsonhalDefinitionRead
from jsonhub_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jsonhub_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = jsonhub_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jsonhub_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jsonhub_sdk.DefinitionApi(api_client)
    id = 'id_example' # str | definition identifier
    definition_definition_write = jsonhub_sdk.DefinitionDefinitionWrite() # DefinitionDefinitionWrite | The updated definition resource

    try:
        # Updates the definition resource.
        api_response = api_instance.api_definitions_id_patch(id, definition_definition_write)
        print("The response of DefinitionApi->api_definitions_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefinitionApi->api_definitions_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| definition identifier | 
 **definition_definition_write** | [**DefinitionDefinitionWrite**](DefinitionDefinitionWrite.md)| The updated definition resource | 

### Return type

[**DefinitionJsonhalDefinitionRead**](DefinitionJsonhalDefinitionRead.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json, application/vnd.api+json
 - **Accept**: application/hal+json, application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | definition resource updated |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_definitions_post**
> DefinitionJsonhalDefinitionRead api_definitions_post(definition_jsonhal_definition_write)

Creates a definition resource.

Creates a definition resource.

### Example

* Bearer Authentication (access_token):

```python
import jsonhub_sdk
from jsonhub_sdk.models.definition_jsonhal_definition_read import DefinitionJsonhalDefinitionRead
from jsonhub_sdk.models.definition_jsonhal_definition_write import DefinitionJsonhalDefinitionWrite
from jsonhub_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jsonhub_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = jsonhub_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jsonhub_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jsonhub_sdk.DefinitionApi(api_client)
    definition_jsonhal_definition_write = jsonhub_sdk.DefinitionJsonhalDefinitionWrite() # DefinitionJsonhalDefinitionWrite | The new definition resource

    try:
        # Creates a definition resource.
        api_response = api_instance.api_definitions_post(definition_jsonhal_definition_write)
        print("The response of DefinitionApi->api_definitions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefinitionApi->api_definitions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definition_jsonhal_definition_write** | [**DefinitionJsonhalDefinitionWrite**](DefinitionJsonhalDefinitionWrite.md)| The new definition resource | 

### Return type

[**DefinitionJsonhalDefinitionRead**](DefinitionJsonhalDefinitionRead.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/hal+json, application/vnd.api+json
 - **Accept**: application/hal+json, application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | definition resource created |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

