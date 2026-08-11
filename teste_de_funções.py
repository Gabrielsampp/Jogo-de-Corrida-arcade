from Entidades.Admin.get import get

dados = get()  # Chama a função get() para obter os dados dos administradores

for adms in dados:
    print(f"Nome de usuário: {adms['nome_usuario']}") # printa o nome de usuário do administrador
    print(f"Senha: {adms['senha']}") #printa a senha do administrador
    print("--------------------")