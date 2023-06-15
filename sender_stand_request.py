import configuration
import requests
import data


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def post_new_user_kit(body, auth_token):
    headers_with_token = data.headers.copy()
    headers_with_token["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_KIT_PATH,
                         json=body,
                         headers=headers_with_token)



#response = post_new_user(data.user_body);
#print(response.status_code)
#print(response.json())














