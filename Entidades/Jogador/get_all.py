import json
from pathlib import Path #A biblioteca path ajuda a localizar o arquivo json, mesmo que o programa seja executado em outro diretório.

def get_all(): #função que retorna todos os jogadores registrados no jogador.json
    path = Path(__file__).parent / "jogador.json"

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data["players"]