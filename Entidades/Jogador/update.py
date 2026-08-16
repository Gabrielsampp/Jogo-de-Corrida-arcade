#FUNÇÂO UPDATE - JOGADOR

import json
import os

# Este comando abaixo descobre o endereço do arquivo jogador.json pela lógica de um "caminho relativo"
# Utilizamos pois o caminho absoluto, como aprendemos com o Wesckley, pode mudar de acordo com o SO

FILE = os.path.join(os.path.dirname(__file__), "jogador.json")

# Função update:

def update(nickname, new_data):

    #abre arquivo para leitura e atribui os dados do arquivo a variável dados, tornando-a como um "dicionário".

    with open(FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Verifica se é o jogador e subistitui os dados do dicionário com as diferenças da segunda entrada da função.

    for player in data["jogadores"]:
        if player["nickname"] == nickname:

            player.update(new_data)

            #abre o arquivo para escrita e sobrescreve com os dados que foram modificados acima

            with open(FILE, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

            return True

    return False