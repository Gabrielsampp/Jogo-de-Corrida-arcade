import json

# Importação das funções auxiliares (sem uso de OOP/Classes)
try:
    from Entidades.Ranking.get_all import get_all
    from Entidades.Ranking.delete import remove_player
    from Entidades.Ranking.create import add_player
except ImportError:
    from get_all import get_all
    from delete import remove_player
    from create import add_player


def atualizar(nickname: str, pontuacao: float):

    try:
        # 1. Busca todos os registros (retorna uma lista de dicionários)
        lista_ranking = get_all()

        # 2. Verifica se o jogador já existe na base
        jogador_encontrado = False

        for jogador in lista_ranking:
            if jogador.get("nickname") == nickname or jogador.get("apelido") == nickname:
                jogador_encontrado = True
                break

        # 3. Regra do requisito:
        if jogador_encontrado:
            # Se encontrar: remove e adiciona novamente
            remove_player(nickname)
            add_player(nickname, pontuacao)
            mensagem = f"Desempenho de '{nickname}' atualizado com sucesso!"
        else:
            # Se não encontrar: chama add_player direto
            add_player(nickname, pontuacao)
            mensagem = f"Jogador '{nickname}' não encontrado. Novo registro criado no ranking!"

        return True, mensagem

    except Exception as erro:
        return False, f"Erro ao atualizar o ranking: {str(erro)}"