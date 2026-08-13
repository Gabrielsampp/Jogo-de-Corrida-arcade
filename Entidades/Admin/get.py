import json
from pathlib import Path #A biblioteca path ajuda a localizar o arquivo json, mesmo que o programa seja executado em outro diretório.

def get(): #função que retorna todos os adms registrados no admin.json
    caminho = Path(__file__).parent / "admin.json"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["admins"]
