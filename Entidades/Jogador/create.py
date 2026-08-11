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
    
    
nickname = input("Digite o nickname do jogador: ")
senha = input("Digite a senha do jogador: ")
print(create(nickname, senha))