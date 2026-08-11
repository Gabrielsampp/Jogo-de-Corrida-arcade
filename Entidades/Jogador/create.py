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

    if Valid_nickname and Valid_senha:    
        existencia = get_by_username(nickname)
        if existencia != None:
            return "Nickname já existe. Por favor, escolha outro."
        else:
            if not caminho.exists():
                informacao = {"jogadores": []}
            else:
                with open(caminho, "r", encoding="utf-8") as arquivo:
                    informacao = json.load(arquivo)

            novo_jogador = {
                "nickname": nickname,
                "senha": senha,
                "melhor_pontuacao": 0,
                "pistas": [],
            }
            informacao["jogadores"].append(novo_jogador)
            with open(caminho, "w", encoding="utf-8") as arquivo:
                json.dump(informacao, arquivo, indent=4)

            if get_by_username(nickname) is not None:
                return "Jogador criado com sucesso!"
            else:
                return "Erro: jogador não foi salvo corretamente."
    else:
        return "Nickname ou senha inválidos. Por favor, tente novamente."

print(create(nickname, senha))