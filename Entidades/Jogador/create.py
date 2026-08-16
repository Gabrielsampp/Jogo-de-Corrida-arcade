from Entidades.Jogador.get_by_user_name import get_by_username
from pathlib import Path
import json

path = Path(__file__).parent / "jogador.json"

def create(nickname,password): 
    #validação do nickname
    Valid_nickname = False
    nickname = nickname.strip()
    if len(nickname) < 1:
        Valid_nickname = False
    elif len(nickname) > 10:
        Valid_nickname = False
    else:
        Valid_nickname = True

    #validação da password
    Valid_password = False
    password = password.strip()
    if len(password) < 3:
        Valid_password = False
    elif len(password) > 10:
        Valid_password = False
    else:
        Valid_password = True

    #Validação e criação do jogador
    if Valid_nickname and Valid_password:  #Caso o nickname e a senha sejam válidos, cria o jogador  
        exists = get_by_username(nickname)
        if exists != None: #Verifica se o nickname já existe
            return "Nickname já existe. Por favor, escolha outro."
        else:
            if not path.exists(): #Caso seja a primeira vez que o arquivo é criado, cria um dicionário vazio
                info = {"players": []}
            else: #Caso o arquivo já exista, lê o conteúdo do arquivo JSON com a codificação UTF-8 que permite acentuação e caracteres especiais
                with open(path, "r", encoding="utf-8") as file:
                    info = json.load(file) 
            #Dicionário com as informações do novo jogador, incluindo nickname, senha, melhor pontuação e lista de pistas
            new_player = {
                "nickname": nickname,
                "password": password,
                "best_score": 0,
                "tracks": [],
            }
            info["players"].append(new_player) #Com o o dicionário criado, adiciona o novo jogador à lista de players
            with open(path, "w", encoding="utf-8") as arquivo: #Abre o arquivo JSON para escrita com a codificação UTF-8 que permite acentuação e caracteres especiais
                json.dump(info, file, indent=4) #Salva o conteúdo atualizado no arquivo JSON, com indentação de 4 espaços para melhor legibilidade

            if get_by_username(nickname) is not None: #Verifica se o jogador foi criado com sucesso
                return "Jogador criado com sucesso!"
            else:
                return "Erro: jogador não foi salvo corretamente."
    else: #Caso o nickname ou a senha sejam inválidos, retorna uma mensagem de erro
        return "Nickname ou senha inválidos. Por favor, tente novamente."

# print(create(nickname, senha))