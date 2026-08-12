from pathlib import Path
import json

def buscar_pistas_por_id (lista_ids):
    with open("pista.json", "r", encoding= "utf-8") as info_pistas:
        lista_pistas = json.load(info_pistas)
        pistas_encontradas = []
    
        for pista in lista_pistas["pistas"]:
            if pista["id"] in lista_ids:
                pistas_encontradas.append(pista)

    return pistas_encontradas

lista_ids = [1, 2, 3]  # Exemplo de lista de IDs
pistas_encontradas = buscar_pistas_por_id(lista_ids)
print (pistas_encontradas)