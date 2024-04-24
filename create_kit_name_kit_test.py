import sender_stand_request
import data

# Función para cambiar el valor del parámetro name en el cuerpo de la solicitud
def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()  # Copia el cuerpo de la solicitud desde el archivo de datos
    current_kit_body["name"] = kit_name  # Se cambia el valor del parámetro name
    return current_kit_body  # Se regresa un nuevo diccionario con el valor kit_name requerido

# Función para obtener y guardar el valor del authToken del nuevo usuario creado
def get_auth_token():
    user_body = data.user_body  # Asegúrate de que esto esté correctamente definido en data.py
    user_response = sender_stand_request.post_new_user(user_body) # Crea un usuario nuevo
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != "" # Verifica que el campo authToken está en la respuesta y contiene un valor
    auth_token = user_response.json().get("authToken")  # Guarda el valor del token del usuario en la variable auth_token
    assert auth_token != ""  # Verifica que se obtuvo el authToken
    print(auth_token)  # Imprime el valor del auth_token para verificar su valor
    return auth_token


# Función de prueba positiva para creación de kit
def positive_assert_kit_name(kit_name):
    auth_token = get_auth_token()  # El valor del token se guarda en la variable auth_token
    kit_body = get_kit_body(kit_name)  # El cuerpo de la solicitud se guarda la variable kit_body

    # El resultado de la solicitud para crear un kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_kit(kit_body, auth_token)
    assert kit_response.status_code == 201  # Comprueba si el código de estado es 201

    # CORRECCION. Combrueba que el campo name del cuerpo de la respuesta coincida con el del cuerpo de la solicitud.
    assert kit_response.json()["name"] == kit_name
    print(kit_response.text)  # Imprime el valor del kit creado para comprobar que utiliza el auth_token generado


# Función de prueba negativa con error 400 para creación de kit
def negative_assert_code_400(kit_name):
    auth_token = get_auth_token()
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_kit(kit_body, auth_token)
    assert kit_response.status_code == 400   # Comprueba si el código de estado es 400
    assert kit_response.json()["code"] == 400   # Comprueba que el atributo code en el cuerpo de respuesta es 400


# Función de prueba negativa para creación de kit sin nombre
def negative_assert_no_kit_name(kit_body):
    auth_token = get_auth_token()
    kit_response = sender_stand_request.post_new_kit(kit_body, auth_token)
    assert kit_response.status_code == 400  # Comprueba si el código de estado es 400
    assert kit_response.json()["code"] == 400  # Comprueba que el atributo code en el cuerpo de respuesta es 400


# Prueba 1. Kit creado con éxito. El parámetro name contiene 1 caracter.
def test1_create_kit_1_character_in_kit_name_get_success_response():
    positive_assert_kit_name("Ddd")


# Prueba 2. Kit creado con éxito. El número permitido de caracteres es 511.
def test2_create_kit_511_character_in_kit_name_get_success_response():
    positive_assert_kit_name(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Prueba 3. Error. El parámetro contiene un string vacío.
def test3_create_kit_0_character_in_kit_name_get_error_response():
    negative_assert_code_400("")


# Prueba 4. Error. El número de caracteres es mayor que la cantidad permitida (512).
def test4_create_kit_512_character_in_kit_name_get_error_response():
    negative_assert_code_400(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Prueba 5. Kit creado con éxito. Se permiten caracteres especiales en el parámetro name.
def test5_create_kit_symbol_in_kit_name_get_success_response():
    positive_assert_kit_name("Ñ$%&/(@")


# Prueba 6. Kit creado con éxito. Se permiten espacios en el parámetro name.
def test6_create_kit_space_in_kit_name_get_success_response():
    positive_assert_kit_name(" A Aaa ")


# Prueba 7. Kit creado con éxito. Se permiten strings números en el parámetro name.
def test7_create_kit_numbers_in_kit_name_get_success_response():
    positive_assert_kit_name("123")


# Prueba 8. Error. Falta el parámetro name en la solicitud.
def test8_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name", None)
    negative_assert_no_kit_name(kit_body)


# Prueba 9. Error. El tipo del parámetro name es numerico.
def test9_create_kit_number_type_name_get_error_response():
    negative_assert_code_400(567)

