import json
from pathlib import Path

caminho = Path(__file__).parent / "jogador.json"                        #Busca o arquivo jogador.json

with open(caminho, "r", encoding="utf-8") as arquivo:                   #Abre o arquivo.
    dados = json.load(arquivo)                                          #pega o conteúdo do arquivo e transforma em um objeto Python

jogadores = dados["jogadores"]                                          #Pega somente a lista de jogadores.


def login(nickname, senha):
    for jogador in jogadores:
            if jogador["nickname"] == nickname:
                if jogador["senha"] == senha:
                    return True, "Login realizado com sucesso!"
                else:
                    return False, "Senha ou nickname incorretos!"

    return False, "Jogador não encontrado."
    