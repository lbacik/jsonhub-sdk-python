# jsonhub-sdk.Oauth2Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_oauth2token_post**](Oauth2Api.md#api_oauth2token_post) | **POST** /api/oauth2/token | Retrieve an OAuth2 Token


# **api_oauth2token_post**
> Oauth2JsonhalOauth2Read api_oauth2token_post(oauth2_jsonhal_oauth2_write)

Retrieve an OAuth2 Token

This endpoint issues an OAuth2 token using your client credentials.

### Example


```python
import jsonhub-sdk
from jsonhub-sdk.models.oauth2_jsonhal_oauth2_read import Oauth2JsonhalOauth2Read
from jsonhub-sdk.models.oauth2_jsonhal_oauth2_write import Oauth2JsonhalOauth2Write
from jsonhub-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jsonhub-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with jsonhub-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jsonhub-sdk.Oauth2Api(api_client)
    oauth2_jsonhal_oauth2_write = jsonhub-sdk.Oauth2JsonhalOauth2Write() # Oauth2JsonhalOauth2Write | The new oauth2 resource

    try:
        # Retrieve an OAuth2 Token
        api_response = api_instance.api_oauth2token_post(oauth2_jsonhal_oauth2_write)
        print("The response of Oauth2Api->api_oauth2token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Oauth2Api->api_oauth2token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth2_jsonhal_oauth2_write** | [**Oauth2JsonhalOauth2Write**](Oauth2JsonhalOauth2Write.md)| The new oauth2 resource | 

### Return type

[**Oauth2JsonhalOauth2Read**](Oauth2JsonhalOauth2Read.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/hal+json, application/vnd.api+json
 - **Accept**: application/hal+json, application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | oauth2 resource created |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

