import json
from pathlib import Path

caminho = Path(__file__).parent / "pista.json"

def get_all():
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    pistas = dados["pistas"]

    return pistas