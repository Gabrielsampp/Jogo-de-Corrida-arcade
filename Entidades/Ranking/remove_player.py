import json
from pathlib import Path

caminho = Path(__file__).parent / "ranking.json"


def remove_player(nome):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    ranking = dados["ranking"]

    for jogador in ranking:
        if jogador["nome"] == nome:
            ranking.remove(jogador)

            with open(caminho, "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)

            return True, "Jogador removido do ranking"

    return False, "Jogador não encontrado"