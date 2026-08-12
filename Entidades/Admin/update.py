import json

def update(dados_novos):
    campos_validos = ["nome_usuario", "senha"]

    for campo in dados_novos:
        if campo not in campos_validos:
            return False, "Campo inválido: " + campo

        if dados_novos[campo] == "":
            return False, "O campo " + campo + " não pode ficar vazio"

    arquivo = open("Entidades/Admin/admin.json", "r", encoding="utf-8")
    admin = json.load(arquivo)
    arquivo.close()

    for campo in dados_novos:
        admin[campo] = dados_novos[campo]

    arquivo = open("Entidades/Admin/admin.json", "w", encoding="utf-8")
    json.dump(admin, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

    return True, "Atualizado com sucesso"