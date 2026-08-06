import json 
from pathlib import Path

caminho = Path(__file__).parent / "jogador.json" #Busca o arquivo jogador.json

def get_by_username(nickname):                              #Função criada para retornar os dados do jogador a partir de seu nickname
    with open(caminho, "r", encoding="utf-8") as arquivo:   
        data = json.load(arquivo)

    jogadores = data["jogadores"]

    for jogador in jogadores:
        if jogador["nickname"] == nickname:
            return jogador 

    return None