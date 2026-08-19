import json

from pathlib import Path

path = Path(__file__).parent / "admin.json"

def update(new_data):
    valid_fields = ["username", "password"]

    for field in new_data:
        if field not in valid_fields:
            return False, "Campo inválido: " + field

        if new_data[field] == "":
            return False, "O campo " + field + " não pode ficar vazio"

    file = open(path, "r", encoding="utf-8")
    admin = json.load(file)
    file.close()

    for field in new_data:
        admin[field] = new_data[field]

    file = open(path, "w", encoding="utf-8")
    json.dump(admin, file, indent=4, ensure_ascii=False)
    file.close()

    return True, "Atualizado com sucesso"