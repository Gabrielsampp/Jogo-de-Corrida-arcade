from Entidades.Jogador.jogador import get_all as get_all_jogadores
from Entidades.Jogador.jogador import delete as delete_jogador

from Entidades.Pista.pista import get_all as get_all_pistas
from Entidades.Pista.pista import delete as delete_pista

from Entidades.Admin.admin import update as update_admin

from Entidades.Ranking.ranking import get_all as get_all_ranking
from Entidades.Ranking.ranking import delete as delete_ranking
from Entidades.Ranking.ranking import remove_player as remover_do_ranking

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
        print("=" * 40)
        print("         PAINEL DE ADMINSTRAÇÃO")
        print("=" * 40)
        print("1 - Ranking")
        print("2 - Jogadores")
        print("3 - Pistas")
        print("4 - Remover jogador")
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

        opcoes_consulta = [
            (1, get_all_ranking),
            (2, get_all_jogadores),
            (3, get_all_pistas),
        ]

        if opcao in (1, 2, 3):
            for numero, funcao in opcoes_consulta:
                if opcao == numero:
                    resultado = funcao()
                    for jogador in resultado:
                        for key, item in jogador.items():
                            print(f"{key}: {item}")
                    break

        elif opcao == 4:
            while True:
                nickname = input("Nickname do jogador: ").strip()
                if nickname:
                    break
                print("Nickname não pode ser vazio.")

            if input(f"Remover '{nickname}'? (s/n): ").lower() == "s":
                print(delete_jogador(nickname))
                remover_do_ranking(nickname)

        elif opcao == 5:
            while True:
                entrada = input("Id da pista: ").strip()
                if entrada.isdigit():
                    id_pista = int(entrada)
                    break
                print("Id inválido, digite apenas números.")

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
            continue

        input("\nPressione Enter para continuar...")
        limpar_tela()

if __name__ == "__main__":
    sistema_admin()

