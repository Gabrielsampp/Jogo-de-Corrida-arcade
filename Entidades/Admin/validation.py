import json
from pathlib import Path

caminho = Path(__file__).parent / "admin.json"

def validation(nome_usuario, senha):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    admins = dados["admins"]

    for admin in admins:
        if admin["nome_usuario"] == nome_usuario and admin["senha"] == senha:    
            return True

    return False