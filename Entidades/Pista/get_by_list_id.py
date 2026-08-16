from pathlib import Path
import json

path = Path(__file__).parent / "pista.json"

def get_by_list_id (id_list):
    with open(path, "r", encoding= "utf-8") as info_tracks:
        tracks_list = json.load(info_tracks)
        found_tracks = []
    
        for track in tracks_list["tracks"]:
            if track["id"] in id_list:
                found_tracks.append(track)

    return found_tracks

# id_list = [1, 2]  # Exemplo de lista de IDs
# found_tracks = get_by_list_id(id_list)
# print (found_tracks)