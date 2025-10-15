import requests
from requests.auth import HTTPBasicAuth

def consultar_placa_basico(placa: str, usuario: str, senha: str, api_key: str = None):
    """
    Consulta dados básicos do veículo pela placa.
    Usa GET no endpoint /v2/consultarPlaca.
    """
    url = "https://api.consultarplaca.com.br/v2/consultarPlaca"
    params = {
        "placa": placa
    }
    headers = {
        "Accept": "application/json"
    }
    if api_key:
        headers["X-Api-Key"] = api_key

    try:
        response = requests.get(
            url,
            params=params,
            auth=HTTPBasicAuth(usuario, senha),
            headers=headers,
            timeout=20
        )
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erro {response.status_code}: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print("Erro de conexão:", e)
        return None

if __name__ == "__main__":
    placa = "SLS2B70"
    usuario = "talysson39n@gmail.com"
    senha = "Talysson39n@"
    api_key = "f5174f204366ab806e37e9fdd57586ce"  # opcional, se necessário
    resultado = consultar_placa_basico(placa, usuario, senha, api_key)
    print(resultado)
