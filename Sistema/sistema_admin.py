from Entidades.Jogador.jogador import get_all as get_all_jogadores
from Entidades.Jogador.jogador import delete as delete_jogador

from Entidades.Pista.pista import get_all as get_all_pistas
from Entidades.Pista.pista import delete as delete_pista

from Entidades.Admin.admin import update as update_admin

from Entidades.Ranking.ranking import get_all as get_all_ranking
from Entidades.Ranking.ranking import delete as delete_ranking
from Entidades.Ranking.ranking import remove_player as remover_do_ranking


def sistema_admin():
    rodando = True

    while rodando:
        print("\n1-Ranking  2-Jogadores  3-Pistas  4-Remover jogador")
        print("5-Remover pista  6-Remover do ranking  7-Limpar ranking")
        print("8-Atualizar admin  9-Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            continue

        if opcao < 1 or opcao > 9:
            print("Opção fora do intervalo (1 a 9).")
            continue

        if opcao == 1:
            print(get_all_ranking())

        elif opcao == 2:
            print(get_all_jogadores())

        elif opcao == 3:
            print(get_all_pistas())

        elif opcao == 4:
            nickname = input("Nickname do jogador: ").strip()
            if not nickname:
                print("Nickname não pode ser vazio.")
                continue
            if input(f"Remover '{nickname}'? (s/n): ").lower() == "s":
                print(delete_jogador(nickname))
                remover_do_ranking(nickname)

        elif opcao == 5:
            try:
                id_pista = int(input("Id da pista: "))
            except ValueError:
                print("Id inválido.")
                continue
            if input(f"Remover pista {id_pista}? (s/n): ").lower() == "s":
                print(delete_pista(id_pista))

        elif opcao == 6:
            nickname = input("Nickname a remover do ranking: ").strip()
            if not nickname:
                print("Nickname não pode ser vazio.")
                continue
            if input(f"Remover '{nickname}' do ranking? (s/n): ").lower() == "s":
                print(remover_do_ranking(nickname))

        elif opcao == 7:
            if input("Apagar TODO o ranking? (s/n): ").lower() == "s":
                print(delete_ranking())

        elif opcao == 8:
            usuario = input("Novo usuário (Enter p/ manter): ").strip()
            senha = input("Nova senha (Enter p/ manter): ").strip()
            dados = {}
            if usuario:
                dados["nome_usuario"] = usuario
            if senha:
                dados["senha"] = senha
            if dados:
                print(update_admin(dados))
            else:
                print("Nenhuma alteração informada.")

        elif opcao == 9:
            print("Saindo do sistema de admin...")
            rodando = False