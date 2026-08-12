#FUNÇÂO UPDATE - JOGADOR

import json
import os

# Este comando abaixo descobre o endereço do arquivo jogador.json pela lógica de um "caminho relativo"
# Utilizamos pois o caminho absoluto, como aprendemos com o Wesckley, pode mudar de acordo com o SO

caminho = os.path.join(os.path.dirname(__file__), "jogador.json")

# Função update:

def atualizar_jogador(nickname, novos_dados):

    #abre arquivo para leitura e atribui os dados do arquivo a variável dados, tornando-a como um "dicionário".

    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    # Verifica se é o jogador e subistitui os dados do dicionário com as diferenças da segunda entrada da função.

    for jogador in dados["jogadores"]:
        if jogador["nickname"] == nickname:

            jogador.update(novos_dados)

            #abre o arquivo para escrita e sobrescreve com os dados que foram modificados acima

            with open(caminho, "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)

            return True

    return False