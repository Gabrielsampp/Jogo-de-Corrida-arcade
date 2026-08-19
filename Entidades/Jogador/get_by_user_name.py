import json 
from pathlib import Path

path = Path(__file__).parent / "jogador.json" #Busca o arquivo jogador.json

def get_by_username(nickname):                              #Função criada para retornar os dados do jogador a partir de seu nickname
    with open(path, "r", encoding="utf-8") as file:   
        data = json.load(file)

    players = data["players"]

    for player in players:
        if player["nickname"] == nickname:
            return player 

    return None