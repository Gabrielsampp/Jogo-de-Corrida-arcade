import json
from pathlib import Path

path = Path(__file__).parent / "ranking.json"

def add_player(name, score):                               #função para adicionar jogador ao ranking

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    ranking = data["ranking"]

    for player in ranking:                              #verifica se o jogador já está no ranking
        if player["name"] == name: 
            return False, "Jogador já existe"

    new_player = {                                          #se não estiver, cria um novo jogador 
        "name": name,
        "score": score
    }

    position = 0

    while position < len(ranking) and ranking[position]["score"] >= score:      #identifica se o jogador adicionado possui mais ou menos pontos que o primeiro jogador no ranking em diante
                                                                            
        position += 1

    ranking.insert(position, new_player)                                       

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)                     #adiciona o novo jogador ao ranking

    return True, "Jogador adicionado ao ranking"