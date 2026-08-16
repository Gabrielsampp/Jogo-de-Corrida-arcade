#FUNÇÃO CREATE - PISTA

import json
from pathlib import Path
from Entidades.Pista.get_last_id import get_last_id

land_form = ["deserto", "asfalto", "antártida", "campos verdes"] 

#                                                   FUNÇÃO PRINCIPAL
def cadastrar_pista(
    player: str,
    name: str,
    is_public: bool,
    landform: str,
    speed: float,
    obstacles: int,
    color: str,
    # caminho_arquivo: str = "Entidades/Pista/pista.json"
):
    # Relevo                                      Validações de entradas
    if landform.lower() not in land_form:
        return (False, f"Tipo de relevo inválido. Permitidos: {land_form}")
    # Velocidade
    try:
        speed_num = float(speed)
        if speed_num <= 0:
            return (False, "A velocidade deve ser maior que zero.")
    except (ValueError, TypeError):
        return (False, "A velocidade precisa ser um número válido (ex: 15.0).")

    # Obstáculos
    try:
        obstacles_num = int(obstacles)
        if obstacles_num < 0:
            return (False, "A quantidade de obstáculos não pode ser negativa.")
    except (ValueError, TypeError):
        return (False, "A quantidade de obstáculos precisa ser um número inteiro (ex: 5).")

    try: #                                                  Manipulação no arquivo

        last = get_last_id() # Elaboração de um novo ID
        new_id = (last if last is not None else 0) + 1

        new_track = { #                                    Novos dados da pista.
            "id": new_id,
            "name": name,
            "is_public": is_public,
            "land_form": landform,
            "speed": float(speed),
            "obstacles": int(obstacles),
            "best_performance": 0,
            "best_performance_player": player,
            "car": str(color)
        }
        
        data = {"track": []}
        path = Path(__file__).parent / "pista.json"

        # Leitura
        if path.exists():
            with path.open("r", encoding="utf-8") as file:
                content = file.read().strip()

                if content:
                    data = json.loads(content)

                    if "tracks" not in data:
                        data["tracks"] = []

        data["tracks"].append(new_track)

        # Escrita
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        return (True, f"Pista '{name}' cadastrada com sucesso com o ID {new_id}.")

    except Exception as error:
        return (False, f"Falha ao cadastrar a pista: {str(error)}")