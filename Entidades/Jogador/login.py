import json
from pathlib import Path

path = Path(__file__).parent / "jogador.json"                        #Busca o arquivo jogador.json



def login_player(nickname, password):
    with open(path, "r", encoding="utf-8") as file:                   #Abre o arquivo.
        data = json.load(file)                                          #pega o conteúdo do arquivo e transforma em um objeto Python

    players = data["players"]                                          #Pega somente a lista de jogadores.

    for player in players:
        if player["nickname"] == nickname and player["password"] == password:
            return True, "Login realizado com sucesso!"
        
    return False, "Nickname ou senha incorretos!"
    