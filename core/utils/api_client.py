# import requests
# import json
# import pytest
#
#
# import requests
# import json
# import pytest
#
# def get_token():
#     auth_url = "https://dev2.getinfo.radugi.net/api/jwt"
#     auth_data = {
#         "username": "dumbledore@sct.team",
#         "password": "12345678qQ1"
#     }
#     try:
#         response = requests.post(auth_url, json=auth_data)
#         response.raise_for_status()
#         data = response.json()  # Получаем весь JSON-ответ
#         access_token = data.get("token")
#         refresh_token = data.get("refresh_token")
#         if not access_token:
#             raise ValueError("Токен не найден в ответе API")
#         return {
#             "accessToken": access_token,
#             "refreshToken": refresh_token
#         }
#     except Exception as e:
#         pytest.fail(f"Ошибка при получении токена: {str(e)}")


# Не получилось авторизоваться через подтягивание локал сториж или куков ((((