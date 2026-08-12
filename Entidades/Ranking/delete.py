import json
from pathlib import Path

def delete():
    caminho = Path(__file__).parent / "ranking.json"
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    removidos = dados.get("ranking", []) #Recebe a lista ranking.json, caso não exista, recebe uma lista vazia.
    if not removidos:
        return False, "Ranking já vazio" #Condição para caso o ranking já esteja vazio, retornando False e uma mensagem de erro.

    dados["ranking"] = [] #Altera a lista ranking.json para uma lista vazia, removendo todos os elementos.

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False) #Rees
    return True, removidos
