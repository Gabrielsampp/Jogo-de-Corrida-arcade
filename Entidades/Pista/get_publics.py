import json
from pathlib import Path #A biblioteca path ajuda a localizar o arquivo json, mesmo que o programa seja executado em outro diretório.

def get_publics(): #função que retorna todos as pistas registradas no pista.json
    path = Path(__file__).parent / "pista.json"

    with open(path, "r", encoding="utf-8") as file:
        dados = json.load(file)

    return [track for track in dados["tracks"] if track["is_public"] == True] #Retorna as pistas marcadas como "true" na opção "is_public"
