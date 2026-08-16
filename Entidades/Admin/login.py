import json
from pathlib import Path

caminho = Path(__file__).parent / "admin.json" #Busca o arquivo do admin.json

def login(nome_usuario, senha):                           #Função criada para testar a validação do admin         
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    admins = dados["admins"]

    for admin in admins:
        if admin["nome_usuario"] == nome_usuario and admin["senha"] == senha:    #se o usuário e a senha do admin estiverem de acordo com o Json
            return True
                                                                                #retorna True
    return False
