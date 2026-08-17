import json
from pathlib import Path

def delete():
    path = Path(__file__).parent / "ranking.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    removed = data.get("ranking", []) #Recebe a lista ranking.json, caso não exista, recebe uma lista vazia.
    if not removed:
        return False, "Ranking já vazio" #Condição para caso o ranking já esteja vazio, retornando False e uma mensagem de erro.

    data["ranking"] = [] #Altera a lista ranking.json para uma lista vazia, removendo todos os elementos.

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False) #Rees
    return True, removed
