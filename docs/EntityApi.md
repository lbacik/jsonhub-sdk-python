# jsonhub_sdk.EntityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_entities_get_collection**](EntityApi.md#api_entities_get_collection) | **GET** /api/entities | Retrieves the collection of entity resources.
[**api_entities_id_delete**](EntityApi.md#api_entities_id_delete) | **DELETE** /api/entities/{id} | Removes the entity resource.
[**api_entities_id_get**](EntityApi.md#api_entities_id_get) | **GET** /api/entities/{id} | Retrieves a entity resource.
[**api_entities_id_patch**](EntityApi.md#api_entities_id_patch) | **PATCH** /api/entities/{id} | Updates the entity resource.
[**api_entities_post**](EntityApi.md#api_entities_post) | **POST** /api/entities | Creates a entity resource.


# **api_entities_get_collection**
> ApiEntitiesGetCollection200Response api_entities_get_collection(qid=qid, private=private, owned=owned, page=page, limit=limit, properties=properties, definition=definition, parent=parent)

Retrieves the collection of entity resources.

Retrieves the collection of entity resources.

### Example

* Bearer Authentication (access_token):

```python
import jsonhub_sdk
from jsonhub_sdk.models.api_entities_get_collection200_response import ApiEntitiesGetCollection200Response
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
    api_instance = jsonhub_sdk.EntityApi(api_client)
    qid = 'qid_example' # str | Filter by slug/id (partial match) (optional)
    private = True # bool | Show only private entities (owned by the current user) (optional)
    owned = True # bool | Show only entities owned by the current user (optional)
    page = 1 # int | The collection page number (optional) (default to 1)
    limit = 10 # int | The number of items per page (optional) (default to 10)
    properties = ['properties_example'] # List[str] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty} (optional)
    definition = 'definition_example' # str | Filter by definition (uuid) (optional)
    parent = 'parent_example' # str | Filter by parent (uuid) (optional)

    try:
        # Retrieves the collection of entity resources.
        api_response = api_instance.api_entities_get_collection(qid=qid, private=private, owned=owned, page=page, limit=limit, properties=properties, definition=definition, parent=parent)
        print("The response of EntityApi->api_entities_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->api_entities_get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qid** | **str**| Filter by slug/id (partial match) | [optional] 
 **private** | **bool**| Show only private entities (owned by the current user) | [optional] 
 **owned** | **bool**| Show only entities owned by the current user | [optional] 
 **page** | **int**| The collection page number | [optional] [default to 1]
 **limit** | **int**| The number of items per page | [optional] [default to 10]
 **properties** | [**List[str]**](str.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] 
 **definition** | **str**| Filter by definition (uuid) | [optional] 
 **parent** | **str**| Filter by parent (uuid) | [optional] 

### Return type

[**ApiEntitiesGetCollection200Response**](ApiEntitiesGetCollection200Response.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | entity collection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_entities_id_delete**
> api_entities_id_delete(id)

Removes the entity resource.

Removes the entity resource.

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
    api_instance = jsonhub_sdk.EntityApi(api_client)
    id = 'id_example' # str | entity identifier

    try:
        # Removes the entity resource.
        api_instance.api_entities_id_delete(id)
    except Exception as e:
        print("Exception when calling EntityApi->api_entities_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| entity identifier | 

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
**204** | entity resource deleted |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_entities_id_get**
> EntityJsonhalEntityReadEntityReadParent api_entities_id_get(id)

Retrieves a entity resource.

Retrieves a entity resource.

### Example

* Bearer Authentication (access_token):

```python
import jsonhub_sdk
from jsonhub_sdk.models.entity_jsonhal_entity_read_entity_read_parent import EntityJsonhalEntityReadEntityReadParent
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
    api_instance = jsonhub_sdk.EntityApi(api_client)
    id = 'id_example' # str | entity identifier

    try:
        # Retrieves a entity resource.
        api_response = api_instance.api_entities_id_get(id)
        print("The response of EntityApi->api_entities_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->api_entities_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| entity identifier | 

### Return type

[**EntityJsonhalEntityReadEntityReadParent**](EntityJsonhalEntityReadEntityReadParent.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | entity resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_entities_id_patch**
> EntityJsonhalEntityReadEntityReadParent api_entities_id_patch(id, entity_entity_update)

Updates the entity resource.

Updates the entity resource.

### Example

* Bearer Authentication (access_token):

```python
import jsonhub_sdk
from jsonhub_sdk.models.entity_entity_update import EntityEntityUpdate
from jsonhub_sdk.models.entity_jsonhal_entity_read_entity_read_parent import EntityJsonhalEntityReadEntityReadParent
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
    api_instance = jsonhub_sdk.EntityApi(api_client)
    id = 'id_example' # str | entity identifier
    entity_entity_update = jsonhub_sdk.EntityEntityUpdate() # EntityEntityUpdate | The updated entity resource

    try:
        # Updates the entity resource.
        api_response = api_instance.api_entities_id_patch(id, entity_entity_update)
        print("The response of EntityApi->api_entities_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->api_entities_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| entity identifier | 
 **entity_entity_update** | [**EntityEntityUpdate**](EntityEntityUpdate.md)| The updated entity resource | 

### Return type

[**EntityJsonhalEntityReadEntityReadParent**](EntityJsonhalEntityReadEntityReadParent.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json, application/vnd.api+json
 - **Accept**: application/hal+json, application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | entity resource updated |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_entities_post**
> EntityJsonhalEntityReadEntityReadParent api_entities_post(entity_jsonhal_entity_create)

Creates a entity resource.

Creates a entity resource.

### Example

* Bearer Authentication (access_token):

```python
import jsonhub_sdk
from jsonhub_sdk.models.entity_jsonhal_entity_create import EntityJsonhalEntityCreate
from jsonhub_sdk.models.entity_jsonhal_entity_read_entity_read_parent import EntityJsonhalEntityReadEntityReadParent
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
    api_instance = jsonhub_sdk.EntityApi(api_client)
    entity_jsonhal_entity_create = jsonhub_sdk.EntityJsonhalEntityCreate() # EntityJsonhalEntityCreate | The new entity resource

    try:
        # Creates a entity resource.
        api_response = api_instance.api_entities_post(entity_jsonhal_entity_create)
        print("The response of EntityApi->api_entities_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->api_entities_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_jsonhal_entity_create** | [**EntityJsonhalEntityCreate**](EntityJsonhalEntityCreate.md)| The new entity resource | 

### Return type

[**EntityJsonhalEntityReadEntityReadParent**](EntityJsonhalEntityReadEntityReadParent.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/hal+json, application/vnd.api+json
 - **Accept**: application/hal+json, application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | entity resource created |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

