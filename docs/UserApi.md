# jsonhub-sdk.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_users_id_delete**](UserApi.md#api_users_id_delete) | **DELETE** /api/users/{id} | Removes the user resource.
[**api_users_id_patch**](UserApi.md#api_users_id_patch) | **PATCH** /api/users/{id} | Updates the user resource.
[**api_users_post**](UserApi.md#api_users_post) | **POST** /api/users | Creates a user resource.
[**api_usersresend_activation_post**](UserApi.md#api_usersresend_activation_post) | **POST** /api/users/resend-activation | Resend activation email
[**api_usersreset_password_post**](UserApi.md#api_usersreset_password_post) | **POST** /api/users/reset-password | Reset password (with token)
[**api_userssend_reset_password_post**](UserApi.md#api_userssend_reset_password_post) | **POST** /api/users/send-reset-password | Send reset password email


# **api_users_id_delete**
> api_users_id_delete(id)

Removes the user resource.

Removes the user resource.

### Example

* Bearer Authentication (access_token):

```python
import jsonhub-sdk
from jsonhub-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jsonhub-sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = jsonhub-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jsonhub-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jsonhub-sdk.UserApi(api_client)
    id = 'id_example' # str | user identifier

    try:
        # Removes the user resource.
        api_instance.api_users_id_delete(id)
    except Exception as e:
        print("Exception when calling UserApi->api_users_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| user identifier | 

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
**204** | user resource deleted |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_id_patch**
> UserJsonhalUserEmpty api_users_id_patch(id, user_user_update)

Updates the user resource.

Updates the user resource.

### Example

* Bearer Authentication (access_token):

```python
import jsonhub-sdk
from jsonhub-sdk.models.user_jsonhal_user_empty import UserJsonhalUserEmpty
from jsonhub-sdk.models.user_user_update import UserUserUpdate
from jsonhub-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jsonhub-sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = jsonhub-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jsonhub-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jsonhub-sdk.UserApi(api_client)
    id = 'id_example' # str | user identifier
    user_user_update = jsonhub-sdk.UserUserUpdate() # UserUserUpdate | The updated user resource

    try:
        # Updates the user resource.
        api_response = api_instance.api_users_id_patch(id, user_user_update)
        print("The response of UserApi->api_users_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_users_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| user identifier | 
 **user_user_update** | [**UserUserUpdate**](UserUserUpdate.md)| The updated user resource | 

### Return type

[**UserJsonhalUserEmpty**](UserJsonhalUserEmpty.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json, application/vnd.api+json
 - **Accept**: application/hal+json, application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | user resource updated |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_post**
> UserJsonhalUserRead api_users_post(user_jsonhal_user_create)

Creates a user resource.

Creates a user resource.

### Example


```python
import jsonhub-sdk
from jsonhub-sdk.models.user_jsonhal_user_create import UserJsonhalUserCreate
from jsonhub-sdk.models.user_jsonhal_user_read import UserJsonhalUserRead
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
    api_instance = jsonhub-sdk.UserApi(api_client)
    user_jsonhal_user_create = jsonhub-sdk.UserJsonhalUserCreate() # UserJsonhalUserCreate | The new user resource

    try:
        # Creates a user resource.
        api_response = api_instance.api_users_post(user_jsonhal_user_create)
        print("The response of UserApi->api_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_jsonhal_user_create** | [**UserJsonhalUserCreate**](UserJsonhalUserCreate.md)| The new user resource | 

### Return type

[**UserJsonhalUserRead**](UserJsonhalUserRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/hal+json, application/vnd.api+json
 - **Accept**: application/hal+json, application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | user resource created |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_usersresend_activation_post**
> api_usersresend_activation_post(user_jsonhal_user_resend_activation)

Resend activation email

This endpoint resends the activation email to the user.

### Example


```python
import jsonhub-sdk
from jsonhub-sdk.models.user_jsonhal_user_resend_activation import UserJsonhalUserResendActivation
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
    api_instance = jsonhub-sdk.UserApi(api_client)
    user_jsonhal_user_resend_activation = jsonhub-sdk.UserJsonhalUserResendActivation() # UserJsonhalUserResendActivation | The new user resource

    try:
        # Resend activation email
        api_instance.api_usersresend_activation_post(user_jsonhal_user_resend_activation)
    except Exception as e:
        print("Exception when calling UserApi->api_usersresend_activation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_jsonhal_user_resend_activation** | [**UserJsonhalUserResendActivation**](UserJsonhalUserResendActivation.md)| The new user resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/hal+json, application/vnd.api+json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content. |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_usersreset_password_post**
> api_usersreset_password_post(user_jsonhal_user_reset_password)

Reset password (with token)

This endpoint resets the password of the user using the token sent by email.

### Example


```python
import jsonhub-sdk
from jsonhub-sdk.models.user_jsonhal_user_reset_password import UserJsonhalUserResetPassword
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
    api_instance = jsonhub-sdk.UserApi(api_client)
    user_jsonhal_user_reset_password = jsonhub-sdk.UserJsonhalUserResetPassword() # UserJsonhalUserResetPassword | The new user resource

    try:
        # Reset password (with token)
        api_instance.api_usersreset_password_post(user_jsonhal_user_reset_password)
    except Exception as e:
        print("Exception when calling UserApi->api_usersreset_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_jsonhal_user_reset_password** | [**UserJsonhalUserResetPassword**](UserJsonhalUserResetPassword.md)| The new user resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/hal+json, application/vnd.api+json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content. |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_userssend_reset_password_post**
> api_userssend_reset_password_post(user_jsonhal_user_send_reset_password)

Send reset password email

This endpoint sends a reset password email to the user.

### Example


```python
import jsonhub-sdk
from jsonhub-sdk.models.user_jsonhal_user_send_reset_password import UserJsonhalUserSendResetPassword
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
    api_instance = jsonhub-sdk.UserApi(api_client)
    user_jsonhal_user_send_reset_password = jsonhub-sdk.UserJsonhalUserSendResetPassword() # UserJsonhalUserSendResetPassword | The new user resource

    try:
        # Send reset password email
        api_instance.api_userssend_reset_password_post(user_jsonhal_user_send_reset_password)
    except Exception as e:
        print("Exception when calling UserApi->api_userssend_reset_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_jsonhal_user_send_reset_password** | [**UserJsonhalUserSendResetPassword**](UserJsonhalUserSendResetPassword.md)| The new user resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/hal+json, application/vnd.api+json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content. |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

