import time
from Entidades.Ranking.get_all import get_all
from Entidades.Jogador.login import login_player
from Entidades.Admin.login import login_admin
from Sistema.sistema_admin import sistema_admin
from Sistema.sistema_jogador import sistema_jogador


def main_menu():

    while True:

        print("     MENU INICIAL   ")
        print("====================")
        print("1. Fechar sistema")
        print("2. Logar como adm")
        print("3. Logar como jogador")
        print("4. Ver ranking geral")
        print("====================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Encerrando o sistema...")
            break

        elif opcao == "2":
            print("Login de admin")
            username = input("Nome de usuário: ")
            password = input("Senha: ")

            if login_admin(username, password):
                print("Login realizado com sucesso!")
                sistema_admin()
            else:
                print("Usuário ou senha incorretos.")

        elif opcao == "3":
            print("Login de jogador")

            nickname = input("Nome de usuário: ")
            password = input("Senha: ")

            resultado = login_player(nickname, password)

            if resultado[0]:
                print("Login realizado com sucesso!")

                jogador_atual = resultado[1]

                sistema_jogador(jogador_atual)
            else:
                print("Usuário ou senha incorretos.")

        elif opcao == "4":
            ranking = get_all()

            print("\n==========RANKING==========")

            for posicao, jogador in enumerate(ranking, start=1):
                print(
                    f"{posicao}º - "
                    f"{jogador['nickname']} - "
                    f"{jogador['score']} pontos"
                )
            print("===========================\n")

        else:
            print("Opção inválida.")

            
if __name__ == "__main__":
    main_menu()