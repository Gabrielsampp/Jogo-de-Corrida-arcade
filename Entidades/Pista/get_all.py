import json
from pathlib import Path

caminho = Path(__file__).parent / "pista.json"  #Busca o arquivo pista.json 

def get_all():                                              #função criada para buscar todas as pistas e os suas informações
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    pistas = dados["pistas"]

    return pistas