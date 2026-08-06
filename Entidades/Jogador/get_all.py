import json
from pathlib import Path #A biblioteca path ajuda a localizar o arquivo json, mesmo que o programa seja executado em outro diretório.

def listar_jogadores(): #função que retorna uma lista com os nicknames de todos os jogadores cadastrados no arquivo jogador.json
    caminho = Path(__file__).parent / "jogador.json"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        jogadores = json.load(arquivo)

    return [jogador["nickname"] for jogador in jogadores]