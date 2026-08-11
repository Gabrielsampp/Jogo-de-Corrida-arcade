import json
from pathlib import Path #A biblioteca path ajuda a localizar o arquivo json, mesmo que o programa seja executado em outro diretório.

def get_publics(): #função que retorna todos as pistas registradas no pista.json
    caminho = Path(__file__).parent / "pista.json"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return [pista for pista in dados["pistas"] if pista["is_public"] == True] #Retorna as pistas marcadas como "true" na opção "is_public"
