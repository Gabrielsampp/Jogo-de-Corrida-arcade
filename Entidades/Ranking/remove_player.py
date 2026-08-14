import json
from pathlib import Path

caminho = Path(__file__).parent / "ranking.json"


def remove_player(nome):                                    #função para remover player do ranking
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    ranking = dados["ranking"]

    for jogador in ranking:                                         #busca o nome do jogador no ranking, se encontrar, ele remove do ranking
        if jogador["nome"] == nome:
            ranking.remove(jogador)

            with open(caminho, "w", encoding="utf-8") as arquivo:               #alteração do arquivo
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)

            return True, "Jogador removido do ranking"

    return False, "Jogador não encontrado"