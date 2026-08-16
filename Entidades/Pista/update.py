
import json

path = "Entidades/Pista/pista.json"     # Caminho do arquivo

# Função que atualiza os dados de uma pista com base no id;
def update(id, new_data):

    # Abrindo do arquivo em modo de leitura para recuperar os dados
    file = open(path, 'r', encoding="utf-8")

    data = json.load(file)
    file.close()

    for track in data["tracks"]:
        if track["id"] == id:
            # Abrindo o arquivo em modo de escrita para alterar os dados
            
            file = open(path, 'w', encoding="utf-8")

            track.update(new_data)

            json.dump(data, file, indent=4, ensure_ascii=False)     # Atualizando o arquivo .json

            file.close()
            return True, "Atualizado com sucesso"

    file.close()
    return False, "Pista não encontrada"

            
