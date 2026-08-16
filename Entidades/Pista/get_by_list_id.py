from pathlib import Path
import json
import os


def buscar_pistas_por_id(lista_ids):
    CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), "pista.json")

    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as info_pistas:
        lista_pistas = json.load(info_pistas)

    pistas_encontradas = []

    for pista in lista_pistas["pistas"]:
        if pista["id"] in lista_ids:
            pistas_encontradas.append(pista)

    return pistas_encontradas


if __name__ == "__main__":
    lista_ids = [1, 2]
    pistas_encontradas = buscar_pistas_por_id(lista_ids)
    print(pistas_encontradas)