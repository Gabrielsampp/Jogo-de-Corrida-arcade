from Entidades.Jogador import jogador
from Entidades.Pista import pista
from Entidades.Admin import admin
from Entidades.Ranking import ranking

import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def sistema_admin():
    rodando = True

    while rodando:
        # print("\n1-Ranking  2-Jogadores  3-Pistas  4-Remover jogador")
        # print("5-Remover pista  6-Remover do ranking  7-Limpar ranking")
        # print("8-Atualizar admin  9-Sair")
        print("\n" + "=" * 40)
        print(f"      PAINEL DO ADMIN")
        print("=" * 40)
        print("1 - Ranking")
        print("2 - Jogadores")
        print("3 - Pistas")
        print("4 - Remover Jogador")
        print("5 - Remover pista")
        print("6 - Remover do ranking")
        print("7 - Limpar ranking")
        print("8 - Atualizar admin")
        print("9 - Sair")
        print("=" * 40)

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            continue

        if opcao < 1 or opcao > 9:
            print("Opção fora do intervalo (1 a 9).")
            continue

        # opcoes_consulta = [
        #     (1, get_all_ranking),
        #     (2, get_all_jogadores),
        #     (3, get_all_pistas),
        # ]

        # if opcao in (1, 2, 3):
        #     for numero, funcao in opcoes_consulta:
        #         if opcao == numero:
        #             resultado = funcao()
        #             for jogador in resultado:
        #                 for key, item in jogador.items():
        #                     print(f"{key}: {item}")
        #             break

        if opcao == 1:
            print("\n--- RANKING GERAL ---")
            ranking_dados = ranking.get_all()

            if not ranking_dados:
                print("Nenhuma pontuação registrada ainda.")
            else:
                for posicao, reg in enumerate(ranking_dados, start=1):
                    nome_jogador = reg.get("nickname")
                    score = reg.get("score")
                    print(f"{posicao}º Lugar | Jogador: {nome_jogador} | Pontos: {score}")


        if opcao == 2:
            print("\n--- JOGADORES CADASTRADOS ---")
            all_jogadores = jogador.get_all()

            if not all_jogadores:
                print("Nenhum jogador cadastrado.")
            else:
                for posicao, j in enumerate(all_jogadores, start=1):
                    print(f"| {posicao}º | Nickname: {j.get("nickname", "N/A")}")

        if opcao == 3:
            print("\n--- PISTAS CADASTRADAS ---")
            all_pistas = pista.get_all()

            if not all_pistas:
                print("Nenhuma pista cadastrada.")
            else:
                for p in all_pistas:
                    print(f"| {p.get("id")} | Nome: {p.get("name", "N/A")} | Recorde da pista: {p.get("best_performance")}" )

        elif opcao == 4:
            while True:
                nickname = input("Nickname do jogador: ").strip()
                if nickname:
                    break
                print("Nickname não pode ser vazio.")

            if input(f"Remover '{nickname}'? (s/n): ").lower() == "s":
                print(jogador.delete(nickname))
                ranking.remove_player(nickname)

        elif opcao == 5:
            while True:
                entrada = input("Id da pista: ").strip()
                if entrada.isdigit():
                    id_pista = int(entrada)
                    break
                print("Id inválido, digite apenas números.")

            if input(f"Remover pista {id_pista}? (s/n): ").lower() == "s":
                print(pista.delete(id_pista))
                

        elif opcao == 6:
            nickname = input("Nickname a remover do ranking: ").strip()
            if not nickname:
                print("Nickname não pode ser vazio.")
                continue
            if input(f"Remover '{nickname}' do ranking? (s/n): ").lower() == "s":
                print(ranking.remove_player(nickname))

        elif opcao == 7:
            if input("Apagar TODO o ranking? (s/n): ").lower() == "s":
                print(ranking.delete())

        elif opcao == 8:
            usuario = input("Novo usuário (Enter p/ manter): ").strip()
            senha = input("Nova senha (Enter p/ manter): ").strip()
            dados = {}
            if usuario:
                dados["username"] = usuario
            if senha:
                dados["password"] = senha
            if dados:
                print(admin.update(dados))
            else:
                print("Nenhuma alteração informada.")

        elif opcao == 9:
            print("Saindo do sistema de admin...")
            rodando = False
            continue

        input("\nPressione Enter para continuar...")
        limpar_tela()

# if __name__ == "_main_":
#     sistema_admin()