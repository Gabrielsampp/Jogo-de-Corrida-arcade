import json
from pathlib import Path

caminho = Path(__file__).parent / "ranking.json"

def add_player(nome, pontos):                               #função para adicionar jogador ao ranking

    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    ranking = dados["ranking"]

    for jogador in ranking:                              #verifica se o jogador já está no ranking
        if jogador["nome"] == nome: 
            return False, "Jogador já existe"

    novo_jogador = {                                          #se não estiver, cria um novo jogador 
        "nome": nome,
        "pontos": pontos
    }

    posicao = 0

    while posicao < len(ranking) and ranking[posicao]["pontos"] >= pontos:      #identifica se o jogador adicionado possui mais ou menos pontos que o primeiro jogador no ranking em diante
                                                                            
        posicao += 1

    ranking.insert(posicao, novo_jogador)                                       

    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)                     #adiciona o novo jogador ao ranking

    return True, "Jogador adicionado ao ranking"