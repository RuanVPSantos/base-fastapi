import requests

def fetch_weather_data(api_url: str, api_key: str, city: str) -> dict:
    """
    Busca dados climáticos de uma API externa.
    """
    try:
        response = requests.get(f"{api_url}?q={city}&appid={api_key}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erro ao buscar dados climáticos: {e}")
        return {}

def send_notification(api_url: str, payload: dict, headers: dict) -> bool:
    """
    Envia uma notificação para um endpoint externo.
    """
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        print(f"Erro ao enviar notificação: {e}")
        return False
