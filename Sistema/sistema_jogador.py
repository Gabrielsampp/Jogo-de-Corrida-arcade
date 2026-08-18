# SISTEMA JOGADOR

import sys
from pathlib import Path

# CAMINHO RELATIVO
RAIZ_PROJETO = Path(__file__).resolve().parent.parent
if str(RAIZ_PROJETO) not in sys.path:
    sys.path.append(str(RAIZ_PROJETO))

from Entidades.Pista import pista # importando o módulo
from Entidades.Jogador.update import update
from Entidades.Ranking.get_all import get_all
from Jogo.tela_pista import tela_pista

# FUNÇÃO PRINCIPAL
def sistema_jogador(jogador_atual):

    nickname = jogador_atual["nickname"]

    while True:
        print("\n" + "=" * 40)
        print(f"      PAINEL DO JOGADOR - {nickname.upper()}")
        print("=" * 40)
        print("1 - Jogar")
        print("2 - Criar pista")
        print("3 - Pistas da comunidade")
        print("4 - Alterar senha")
        print("5 - Ver minhas pistas")
        print("6 - Remover pista")
        print("7 - Ver ranking")
        print("8 - Sair do sistema de jogador")
        print("=" * 40)

        opcao = input("Escolha uma opção (1-8): ").strip()

        # 1 - JOGAR
        if opcao == "1":
            pistas_jogador = pista.get_by_list_id(jogador_atual.get("pistas", []))

            print("\n--- SUAS PISTAS ---")
            if not pistas_jogador:
                print("Você ainda não possui pistas registradas.")
            else:
                for p in pistas_jogador:
                    print(f"ID: {p.get('id')} | Nome: {p.get('name')}")

            print("\nComo deseja jogar?")
            print("1. Jogo casual (pista padrão)")
            print("2. Informar ID da pista que está escolhendo")
            escolha = input("Opção: ").strip()

            if escolha == "1":
                print("\nIniciando Jogo Casual na Pista Padrão...")
                tela_pista(pista_id=0)

            elif escolha == "2":
                try:
                    pista_id = int(input("Informe o ID da pista: "))
                    if pista_id in jogador_atual.get("pistas", []):
                        print(f"\nIniciando jogo na pista ID {pista_id}...")
                        tela_pista(pista_id=pista_id)
                    else:
                        print("\n[!] Erro: Pista não encontrada na sua lista.")
                except ValueError:
                    print("\n[!] Digite um ID numérico válido.")

        # 2 - CRIAR PISTA
        elif opcao == "2":
            print("\n--- CRIAR NOVA PISTA ---")

            nome = input("Digite o nome da pista: ").strip()

            print("\nOpções de relevo disponíveis: deserto, asfalto, antártida, campos verdes")
            landform = input("Escolha o tipo de relevo: ").strip()

            velocidade = input("Digite a velocidade (ex: 15.0): ").strip()
            obstaculos = input("Digite a quantidade de obstáculos (ex: 5): ").strip()
            cor = input("Digite a cor do carro: ").strip()

            publica_input = input("A pista será pública? (s/n): ").strip().lower()
            is_public = publica_input == "s"

            # Chama a função create do módulo pista
            sucesso, msg = pista.create(
                player=nickname,
                name=nome,
                is_public=is_public,
                landform=landform,
                speed=velocidade,
                obstacles=obstaculos,
                color=cor
            )

            if sucesso:
                # Recupera o ID que acabou de ser cadastrado
                novo_id = pista.get_last_id()

                if "pistas" not in jogador_atual:
                    jogador_atual["pistas"] = []

                # Vincula o ID à lista do jogador e atualiza no arquivo do jogador
                jogador_atual["pistas"].append(novo_id)
                update(nickname, {"pistas": jogador_atual["pistas"]})

                print(f"\n[+] Sucesso: {msg}")
            else:
                print(f"\n[!] Falha ao cadastrar: {msg}")

        # 3 - PISTAS DA COMUNIDADE
        elif opcao == "3":
            print("\n--- PISTAS DA COMUNIDADE ---")
            pistas_publicas = pista.get_publics()

            if not pistas_publicas:
                print("Nenhuma pista pública disponível no momento.")
            else:
                for p in pistas_publicas:
                    print(f"ID: {p.get('id')} | Criador: {p.get('player', 'Desconhecido')} | Nome: {p.get('name')}")

                try:
                    pista_id = int(input("\nInforme o ID da pista pública para jogar: "))
                    ids_publicos = [p.get("id") for p in pistas_publicas]

                    if pista_id in ids_publicos:
                        print(f"\nIniciando jogo na pista pública ID {pista_id}...")
                        tela_pista(pista_id=pista_id)
                    else:
                        print("\n[!] O ID informado não é de uma pista pública.")
                except ValueError:
                    print("\n[!] ID inválido.")

        # 4 - ALTERAR SENHA
        elif opcao == "4":
            print("\n--- ALTERAR SENHA ---")
            nova_senha = input("Digite a nova senha: ").strip()

            if nova_senha:
                # O update altera a senha garantindo que o nickname não seja alterado
                sucesso = update(nickname, {"senha": nova_senha})
                if sucesso:
                    jogador_atual["senha"] = nova_senha
                    print("\n[+] Senha alterada com sucesso!")
                else:
                    print("\n[!] Erro ao salvar a nova senha no arquivo.")
            else:
                print("\n[!] A senha não pode ser vazia.")

        # 5 - VER MINHAS PISTAS
        elif opcao == "5":
            print("\n--- MINHAS PISTAS ---")
            pistas_jogador = pista.get_by_list_id(jogador_atual.get("pistas", []))

            if not pistas_jogador:
                print("Você ainda não criou nenhuma pista.")
            else:
                for p in pistas_jogador:
                    print(
                        f"ID: {p.get('id')} | "
                        f"Nome: {p.get('name')} | "
                        f"Velocidade: {p.get('speed')} | "
                        f"Obstáculos: {p.get('obstacles')}"
                    )

        # 6 - REMOVER PISTA
        elif opcao == "6":
            print("\n--- REMOVER PISTA ---")
            try:
                pista_id = int(input("Informe o ID da pista que deseja remover: "))

                if pista_id in jogador_atual.get("pistas", []):
                    # 1. Deleta a pista através do módulo pista
                    sucesso_del, msg_del = pista.delete(pista_id)

                    if sucesso_del:
                        # 2. Remove o ID da lista do jogador
                        jogador_atual["pistas"].remove(pista_id)

                        # 3. Atualiza os dados do jogador
                        update(nickname, {"pistas": jogador_atual["pistas"]})
                        print(f"\n[+] Sucesso: {msg_del}")
                    else:
                        print(f"\n[!] Falha ao remover da base: {msg_del}")
                else:
                    print("\n[!] Esta pista não pertence à sua conta.")
            except ValueError:
                print("\n[!] ID inválido! Digite um número inteiro.")

        # 7 - VER RANKING
        elif opcao == "7":
            print("\n--- RANKING GERAL ---")
            ranking_dados = get_all()

            if not ranking_dados:
                print("Nenhuma pontuação registrada ainda.")
            else:
                for posicao, reg in enumerate(ranking_dados, start=1):
                    print(f"{posicao}º Lugar | Jogador: {reg.get('player')} | Pontos: {reg.get('pontuacao', 0)}")

        # 8 - SAIR DO SISTEMA DE JOGADOR
        elif opcao == "8":
            print(f"\nRetornando ao menu inicial... Até logo, {nickname}!")
            break

        else:
            print("\n[!] Opção inválida! Escolha um número de 1 a 8.")