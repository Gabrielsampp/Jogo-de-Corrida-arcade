def validar_nickname(nickname):
    nickname = nickname.strip()

    if len(nickname) < 3 or len(nickname) > 20:
        return False, "Nickname inválido."

    if not nickname.replace("_", "").isalnum():
        return False, "Use apenas letras, números e _."

    return True, nickname


def validar_senha(senha):
    if len(senha) < 4:
        return False, "Senha muito curta."

    return True, senha