from get_by_user_name import get_by_username
from pathlib import Path
import json

caminho = Path(__file__).parent / "jogador.json"

def create(nickname,senha): 
    #validação do nickname
    Valid_nickname = False
    nickname = nickname.strip()
    if len(nickname) < 1:
        Valid_nickname = False
    elif len(nickname) > 10:
        Valid_nickname = False
    else:
        Valid_nickname = True

    #validação da senha
    Valid_senha = False
    senha = senha.strip()
    if len(senha) < 3:
        Valid_senha = False
    elif len(senha) > 10:
        Valid_senha = False
    else:
        Valid_senha = True

    #Validação e criação do jogador
    if Valid_nickname and Valid_senha:  #Caso o nickname e a senha sejam válidos, cria o jogador  
        existencia = get_by_username(nickname)
        if existencia != None: #Verifica se o nickname já existe
            return "Nickname já existe. Por favor, escolha outro."
        else:
            if not caminho.exists(): #Caso seja a primeira vez que o arquivo é criado, cria um dicionário vazio
                informacao = {"jogadores": []}
            else: #Caso o arquivo já exista, lê o conteúdo do arquivo JSON com a codificação UTF-8 que permite acentuação e caracteres especiais
                with open(caminho, "r", encoding="utf-8") as arquivo:
                    informacao = json.load(arquivo) 
            #Dicionário com as informações do novo jogador, incluindo nickname, senha, melhor pontuação e lista de pistas
            novo_jogador = {
                "nickname": nickname,
                "senha": senha,
                "melhor_pontuacao": 0,
                "pistas": [],
            }
            informacao["jogadores"].append(novo_jogador) #Com o o dicionário criado, adiciona o novo jogador à lista de jogadores
            with open(caminho, "w", encoding="utf-8") as arquivo: #Abre o arquivo JSON para escrita com a codificação UTF-8 que permite acentuação e caracteres especiais
                json.dump(informacao, arquivo, indent=4) #Salva o conteúdo atualizado no arquivo JSON, com indentação de 4 espaços para melhor legibilidade

            if get_by_username(nickname) is not None: #Verifica se o jogador foi criado com sucesso
                return "Jogador criado com sucesso!"
            else:
                return "Erro: jogador não foi salvo corretamente."
    else: #Caso o nickname ou a senha sejam inválidos, retorna uma mensagem de erro
        return "Nickname ou senha inválidos. Por favor, tente novamente."

# print(create(nickname, senha))