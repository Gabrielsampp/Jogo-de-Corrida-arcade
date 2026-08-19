import time
from Entidades.Ranking.get_all import get_all
from Entidades.Jogador.login import login_player
from Entidades.Jogador.create import create
from Entidades.Admin.login import login_admin
from Sistema.sistema_admin import sistema_admin
from Sistema.sistema_jogador import sistema_jogador

from Entidades.Jogador import jogador

def main_menu():

    while True:

        print(f"{" "*5}MENU INICIAL{" "*5}")
        print(f"{"="*20}")
        print("1. Fechar sistema")
        print("2. Logar como adm")
        print("3. Logar como jogador")
        print("4. Ver ranking geral")
        print(f"{"="*20}")

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

            print("Escolha uma opção:")
            print("1. Logar como jogador")
            print("2. Cadastrar como jogador")

            opcao_player = input("Escolha uma opção: ")
            if opcao_player == "1":

                print("Login de jogador")

                nickname = input("Nome de usuário: ")
                password = input("Senha: ")

                resultado = login_player(nickname, password)[0]

                if resultado:
                    print("Login realizado com sucesso!")

                    jogador_atual = jogador.get_by_username(nickname)

                    sistema_jogador(jogador_atual)
                else:
                    print("Usuário ou senha incorretos.")

            elif opcao_player == "2":

                print("Cadastro de jogador")

                nickname = input("Escolha um nickname: ")
                password = input("Escolha uma senha: ")

                resultado = create(nickname, password)

                print(resultado)

            else:
                print("Opção inválida.")

        elif opcao == "4":
            ranking = get_all()

            print("==========RANKING==========")

            for posicao, player in enumerate(ranking, start=1):
                print(
                    f"{posicao}º - "
                    f"{player['nickname']} - "
                    f"{player['score']} pontos"
                )
            print("===========================")

        else:
            print("Opção inválida.")

            
if __name__ == "__main__":
    main_menu()