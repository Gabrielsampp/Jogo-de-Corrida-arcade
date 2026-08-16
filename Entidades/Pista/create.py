#FUNÇÃO CREATE - PISTA

import json
from pathlib import Path
from Entidades.Pista.get_last_id import get_last_id

landforms = ["deserto", "asfalto", "antártida", "Campos verdes"] 

def create( #                                       FUNÇÃO PRINCIPAL
    name: str,
    is_public: bool,
    landform: str,
    speed: float,
    obstacles: int,
    color: str,
    path_file: str = "Entidades/Pista/pista.json"
):
    if isinstance(landform, str): #                      Validação dos tipos de relevo                 
        if landform not in landforms:
            return (False, f"Tipo de relevo inválido. Permitidos: {landforms}")
    else:
        return (False, "Formato do tipo de relevo é inválido.")

    try: #                                                  Manipulação no arquivo

        last = get_last_id() #                            Elaboração de um novo ID
        new_id = (last if last is not None else 0) + 1

        new_track = { #                                    Novos dados da pista.
            "id": new_id,
            "name": name,
            "is_public": is_public,
            "tipo_de_relevo": landform,
            "speed": float(speed),
            "obstacles": int(obstacles),
            "best_performance": None,
            "best_performance_player": None,
            "car": str(color)
        }

        data = {"tracks": []}
        path = Path(path_file)

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