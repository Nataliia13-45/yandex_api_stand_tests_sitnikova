import sender_stand_request
import data


def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    return user_response.json()["authToken"]


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_user_kit(kit_body, auth_token)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


def negative_assert_symbol(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_user_kit(kit_body, auth_token)
    assert kit_response.status_code == 400


def negative_assert_empty_kit():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_user_kit(kit_body, auth_token)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Не все необходимые параметры были переданы"


#Tecт 1
def test_create_user_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


#Tecт 2
def test_create_user_kit_511_letter_in_name_get_success_response():
    positive_assert(data.test_511)


# Tecт 3
def test_create_user_0_letter_in_first_name_get_error_response():
    negative_assert_symbol("")


# Tecт 4
def test_create_user_512_letter_in_first_name_get_error_response():
    negative_assert_symbol(data.test_512)


# Tecт 5
def test_create_user_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")


# Tecт 6
def test_create_user_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")


# Tecт 7
def test_create_user_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")


# Tecт 8
def test_create_user_kit_has_space_in_name_get_success_response():
    positive_assert("Человек и КО ")


# Tecт 9
def test_create_user_kit_has_numbers_in_name_get_success_response():
    positive_assert("123")


# Tecт 10
def test_create_user_kit_empty_name_get_error_response():
    negative_assert_empty_kit()


# Tecт 11
def test_create_user_kit_number_type_name_get_error_response():
    negative_assert_symbol(123)
