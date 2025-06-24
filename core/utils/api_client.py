import pytest
import requests


def get_token():
    auth_url = "https://dev2.getinfo.radugi.net/api/jwt"
    auth_data = {
        "username": "dumbledore@sct.team",
        "password": "12345678qQ1"
    }

    try:
        response = requests.post(auth_url, json=auth_data)
        response.raise_for_status()
        token = response.json().get("token")
        if not token:
            raise ValueError("Токен не найден в ответе API")
        else:
            return token
    except Exception as e:
        pytest.fail(f"Ошибка при получении токена: {str(e)}")
