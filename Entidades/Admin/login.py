import json
from pathlib import Path

path = Path(__file__).parent / "admin.json" #Busca o arquivo do admin.json

def login_admin(username, password):                           #Função criada para testar a validação do admin         
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    admin = data

    
    if admin["username"] == username and admin["password"] == password:    #se o usuário e a senha do admin estiverem de acordo com o Json
        return True
                                                                            #retorna True
    return False
