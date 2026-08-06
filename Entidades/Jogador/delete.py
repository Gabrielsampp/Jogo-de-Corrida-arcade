import json
from pathlib import Path

caminho = Path(__file__).parent / "jogador.json"   # Busca o caminho do arquivo json


def get_id_by_nickname(nickname, data):               # Função para buscar a posição do jogador
    for j in data:
        if nickname == j["nickname"]:
            return data.index(j)

    return -1


def delete(nickname=""):
    file = open(caminho, 'r', encoding='utf-8')        # Abrindo o arquivo
    data = json.load(file)                             # Carregando o arquivo em um dicionário.


    pos = get_id_by_nickname(nickname, data["jogadores"])                 # Busca indece do jogador
    file.close()

    if pos != -1:
        data["jogadores"].pop( pos )                            # Removendo jogador

        file = open(caminho, 'w', encoding='utf-8')
        json.dump(data, file, indent=4, ensure_ascii=False)     # Reescrevendo o arquivo json

        file.close()
        return "Jogador removido"
    
    else:
        return "Jogador não encontrado"

