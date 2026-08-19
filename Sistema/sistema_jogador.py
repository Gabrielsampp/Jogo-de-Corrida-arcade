# SISTEMA JOGADOR

import os
import sys
from pathlib import Path

# CAMINHO RELATIVO
RAIZ_PROJETO = Path(__file__).resolve().parent.parent
if str(RAIZ_PROJETO) not in sys.path:
    sys.path.append(str(RAIZ_PROJETO))

from Entidades.Jogador.update import update
from Entidades.Pista import pista
from Entidades.Ranking.get_all import get_all
from Jogo.tela_pista import tela_pista
from Jogo.tela_principal import tela_principal


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# FUNÇÃO PRINCIPAL
def sistema_jogador(jogador_atual):

    nickname = jogador_atual["nickname"]

    while True:
        limpar_tela()
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
            print("ID: 0 | Nome: Pista Padrão (Oficial)")
            if pistas_jogador:
                for p in pistas_jogador:
                    print(f"ID: {p.get('id')} | Nome: {p.get('name')}")

            print("\nComo deseja jogar?")
            print("1. Jogo casual (pista padrão)")
            print("2. Informar ID da pista que está escolhendo")
            escolha = input("Opção: ").strip()

            if escolha == "1":
                print("\nIniciando Jogo Casual na Pista Padrão...")

                pista_padrao = {
                    "id": 0,
                    "name": "Pista Padrão (Oficial)",
                    "is_public": True,
                    "landform": "Campos verdes",
                    "speed": 3,
                    "obstacles": 5,
                    "best_performance": 0,
                    "best_performance_player": "",
                    "car": "azul"
                }

                print("Pista selecionada:")
                print(pista_padrao)

                tela_principal(
                    pista=pista_padrao,
                    jogador=nickname
                )


            elif escolha == "2":
                try:
                    pista_id = int(input("Informe o ID da pista: "))

                    pistas_jogador = pista.get_by_list_id(
                        jogador_atual.get("pistas", [])
                    )

                    pista_escolhida = None

                    for p in pistas_jogador:
                        if p.get("id") == pista_id:
                            pista_escolhida = p
                            break

                    if pista_escolhida is not None:
                        print(f"\nIniciando jogo na pista ID {pista_id}...")

                        tela_principal(
                            pista_escolhida,
                            jogador=nickname
                        )
                    else:
                        print("\n[!] Erro: Pista não encontrada na sua lista.")

                except ValueError:
                    print("\n[!] Digite um ID numérico válido.")

        # 2 - CRIAR PISTA
        elif opcao == "2":
            print("\n--- CRIAR NOVA PISTA ---")

            id_anterior = pista.get_last_id() or 0

            def callback_cadastro(nickname=nickname, **kwargs):
                kwargs["player"] = nickname
                return pista.create(**kwargs)

            tela_pista(callback_cadastro)

            ultimo_id = pista.get_last_id()

            if ultimo_id > id_anterior:
                if "pistas" not in jogador_atual:
                    jogador_atual["pistas"] = []

                # Adiciona o ID da nova pista ao jogador
                jogador_atual["pistas"].append(ultimo_id)

                # Salva a lista atualizada
                sucesso = update(
                    nickname,
                    {"pistas": jogador_atual["pistas"]}
                )

                if sucesso:
                    print(
                        f"\n[+] Pista criada com sucesso!"
                        f"\n    ID da pista: {ultimo_id}"
                    )
                else:
                    print(
                        "\n[!] A pista foi criada, "
                        "mas não foi possível atualizar o jogador."
                    )

            else:
                print("\n[!] Falha ao cadastrar a pista.")


        # 3 - PISTAS DA COMUNIDADE
        elif opcao == "3":
            print("\n--- PISTAS DA COMUNIDADE ---")

            pistas_publicas = pista.get_publics()

            if not pistas_publicas:
                print("Nenhuma pista pública disponível no momento.")
            else:
                for p in pistas_publicas:
                    print(
                        f"ID: {p.get('id')} | "
                        f"Nome: {p.get('name')} | "
                        f"Criador/Recordista: {p.get('best_performance_player', 'N/A')} | "
                        f"Pontos: {p.get('best_performance', 0)} | "
                        f"Relevo: {p.get('landform', 'N/A')} | "
                        f"Velocidade: {p.get('speed', 'N/A')} | "
                        f"Obstáculos: {p.get('obstacles', 'N/A')}"
                    )

                try:
                    pista_id = int(
                        input("\nInforme o ID da pista pública para jogar: ")
                    )

                    # Procura a pista completa pelo ID
                    pista_escolhida = None

                    for p in pistas_publicas:
                        if p.get("id") == pista_id:
                            pista_escolhida = p
                            break

                    if pista_escolhida is not None:
                        print(
                            f"\nIniciando jogo na pista pública ID {pista_id}..."
                        )

                        tela_principal(
                            pista_escolhida,
                            jogador=nickname
                        )

                    else:
                        print(
                            "\n[!] O ID informado não pertence "
                            "a uma pista pública."
                        )

                except ValueError:
                    print("\n[!] Digite um ID numérico válido.")


        # 4 - ALTERAR SENHA
        elif opcao == "4":
            print("\n--- ALTERAR SENHA ---")
            nova_senha = input("Digite a nova senha: ").strip()

            if nova_senha:
                jogador_atual["senha"] = nova_senha
                # Passagem do dicionário atualizado para a função update
                sucesso = update(nickname, jogador_atual)
                if sucesso:
                    print("\n[+] Senha alterada com sucesso!")
                else:
                    print("\n[!] Erro ao salvar a nova senha no arquivo.")
            else:
                print("\n[!] A senha não pode ser vazia.")

        # 5 - VER MINHAS PISTAS
        elif opcao == "5":
            print("\n--- MINHAS PISTAS ---")

            pistas_jogador = pista.get_by_list_id(
                jogador_atual.get("pistas", [])
            )

            if not pistas_jogador:
                print("Você ainda não criou nenhuma pista.")
            else:
                for p in pistas_jogador:
                    pontos = p.get("best_performance", 0)

                    print(
                        f"ID: {p.get('id')} | "
                        f"Nome: {p.get('name')} | "
                        f"Pontos: {pontos} | "
                        f"Relevo: {p.get('landform', 'N/A')} | "
                        f"Velocidade: {p.get('speed', 'N/A')} | "
                        f"Obstáculos: {p.get('obstacles', 'N/A')}"
                    )

        # 6 - REMOVER PISTA
        elif opcao == "6":
            print("\n--- REMOVER PISTA ---")
            try:
                pista_id = int(input("Informe o ID da pista que deseja remover: "))

                if pista_id in jogador_atual.get("pistas", []):
                    sucesso_del, msg_del = pista.delete(pista_id)

                    if sucesso_del:
                        jogador_atual["pistas"].remove(pista_id)
                        update(nickname, jogador_atual)  
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
                    nome_jogador = reg.get("nickname")
                    score = reg.get("score")
                    print(f"{posicao}º Lugar | Jogador: {nome_jogador} | Pontos: {score}")

        # 8 - SAIR DO SISTEMA DE JOGADOR
        elif opcao == "8":
            print(f"\nRetornando ao menu principal... Até logo, {nickname}!")
            input("\nPressione Enter para continuar...")
            limpar_tela()
            break

        else:
            print("\n[!] Opção inválida! Escolha um número de 1 a 8.")

        input("\nPressione Enter para continuar...")