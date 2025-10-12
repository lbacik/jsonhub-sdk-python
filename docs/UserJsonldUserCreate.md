# UserJsonldUserCreate

Create user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 
**activation_url** | **str** |  | [optional] 

## Example

```python
from jsonhub_sdk.models.user_jsonld_user_create import UserJsonldUserCreate

# TODO update the JSON string below
json = "{}"
# create an instance of UserJsonldUserCreate from a JSON string
user_jsonld_user_create_instance = UserJsonldUserCreate.from_json(json)
# print the JSON string representation of the object
print(UserJsonldUserCreate.to_json())

# convert the object into a dict
user_jsonld_user_create_dict = user_jsonld_user_create_instance.to_dict()
# create an instance of UserJsonldUserCreate from a dict
user_jsonld_user_create_from_dict = UserJsonldUserCreate.from_dict(user_jsonld_user_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


