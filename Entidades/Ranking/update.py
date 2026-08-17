import json

# Importação das funções auxiliares (sem uso de OOP/Classes)
try:
    from Entidades.Ranking.get_all import get_all
    from Entidades.Ranking.remove_player import remove_player
    from Entidades.Ranking.add_player import add_player
except ImportError:
    from get_all import get_all
    from delete import remove_player
    from add_player import add_player


def update(nickname: str, score: float):

    try:
        # 1. Busca todos os registros (retorna uma lista de dicionários)
        ranking_list = get_all()

        # 2. Verifica se o jogador já existe na base
        found_player = False

        for player in ranking_list:
            if player.get("nickname") == nickname:
                found_player = True
                break

        # 3. Regra do requisito:
        if found_player:
            # Se encontrar: remove e adiciona novamente
            remove_player(nickname)
            add_player(nickname, score)
            message = f"Desempenho de '{nickname}' atualizado com sucesso!"
        else:
            # Se não encontrar: chama add_player direto
            add_player(nickname, score)
            message = f"Jogador '{nickname}' não encontrado. Novo registro criado no ranking!"

        return True, message

    except Exception as error:
        return False, f"Erro ao atualizar o ranking: {str(error)}"