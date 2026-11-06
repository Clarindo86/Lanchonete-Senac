
import requests

BASE_URL = "https://servicodados.ibge.gov.br/api/v1/localidades"


def buscar_estados():

    resposta = requests.get(
        f"{BASE_URL}/estados",
        params={"orderBy": "nome"},
        timeout=10
    )

    resposta.raise_for_status()

    return resposta.json()


def buscar_municipios(uf_id):

    resposta = requests.get(
        f"{BASE_URL}/estados/{uf_id}/municipios",
        params={"orderBy": "nome"},
        timeout=10
    )

    resposta.raise_for_status()

    return resposta.json()
