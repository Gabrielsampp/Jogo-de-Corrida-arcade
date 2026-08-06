def validar_nickname(nickname):
    nickname = nickname.strip()                                        # Remove espaços no início e no fim

    if len(nickname) < 3 or len(nickname) > 20:                        # Verifica o tamanho permitido
        return False, "Nickname inválido."

    if not nickname.replace("_", "").isalnum():                        # Permite apenas letras, números e "_"
        return False, "Use apenas letras, números e _."

    return True, nickname                                              # Retorna o nickname validado


def validar_senha(senha):
    if len(senha) < 4:
        return False, "Senha muito curta."                             # Verifica se a senha possui o tamanho mínimo

    return True, senha