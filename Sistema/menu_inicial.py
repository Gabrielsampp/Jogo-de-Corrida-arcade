import time
from Entidades.Ranking.get_all import get_all
from Entidades.Jogador.login import login_player
from Entidades.Admin.login import login_admin
# from Entidades.Admin.sistema_admin import sistema_admin
# from Entidades.Jogador.sistema_jogador import sistema_jogador


def main_menu():

    while True:

        print("     MENU INICIAL   ")
        time.sleep(0.2)
        print("====================")
        time.sleep(0.2)
        print("1. Fechar sistema")
        time.sleep(0.2)
        print("2. Logar como adm")
        time.sleep(0.2)
        print("3. Logar como jogador")
        time.sleep(0.2)
        print("4. Ver ranking geral")
        time.sleep(0.2)
        print("====================")
        time.sleep(0.2)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            time.sleep(0.2)
            print("Encerrando o sistema...")
            break

        elif opcao == "2":
            time.sleep(0.2)
            print("Login de admin")
            time.sleep(0.2)
            username = input("Nome de usuário: ")
            time.sleep(0.2)
            password = input("Senha: ")

            if login_admin(username, password):
                time.sleep(0.2)
                print("Login realizado com sucesso!")
                # esperando o sistema admin...
            else:
                time.sleep(0.2)
                print("Usuário ou senha incorretos.")

        elif opcao == "3":
            time.sleep(0.2)
            print("Login de jogador")

            time.sleep(0.2)
            nickname = input("Nome de usuário: ")
            time.sleep(0.2)
            password = input("Senha: ")

            if login_player(nickname, password)[0]:
                time.sleep(0.2)
                print("Login realizado com sucesso!")
                # esperando o sistema jogador...
            else:
                time.sleep(0.2)
                print("Usuário ou senha incorretos.")

        elif opcao == "4":
            ranking = get_all()

            time.sleep(0.2)
            print("\n==========RANKING==========")

            for posicao, jogador in enumerate(ranking, start=1):
                time.sleep(0.2)
                print(
                    f"{posicao}º - "
                    f"{jogador['nickname']} - "
                    f"{jogador['score']} pontos"
                )
                time.sleep(0.2)
            print("===========================\n")

        else:
            print("Opção inválida.")

            
if __name__ == "__main__":
    main_menu()