import json
from pathlib import Path

path = Path(__file__).parent / "ranking.json"


def remove_player(nickname):                                    #função para remover player do ranking
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    ranking = data["ranking"]

    for player in ranking:                                         #busca o nome do jogador no ranking, se encontrar, ele remove do ranking
        if player["nickname"] == nickname:
            ranking.remove(player)

            with open(path, "w", encoding="utf-8") as file:               #alteração do arquivo
                json.dump(data, file, indent=4, ensure_ascii=False)

            return True, "Jogador removido do ranking"

    return False, "Jogador não encontrado"