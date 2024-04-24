import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


response = post_new_user(data.user_body)
print(response.status_code)


def post_new_kit(body, auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}",  # Usar el authToken en el encabezado
        "Content-Type": "application/json"  # Asegúrate de que el Content-Type está definido
    }
    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=body,  # Cuerpo del POST para el kit
        headers=headers  # Encabezados incluyendo el Authorization con el authToken
    )

