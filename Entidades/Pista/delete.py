import json


def delete(track_id):
    try:
        with open("Entidades/Pista/pista.json", "r", encoding="utf-8") as file:                      #Abre o arquivo.
            tracks = json.load(file)                                                                 #pega o conteúdo do arquivo e transforma em um objeto Python
    except:
        return False, "Erro ao acessar a base de dados de pistas"                                       #Erro caso não encontre a pista



    found_tracks = None
    for track in tracks:
        if track["id"] == track_id:                                                                     #Se o id da pista for igual ao encontrado, guarda essa pista
            found_tracks = track
            break



    if found_tracks is None:                                                                        #Caso a pista_encontrada continue "none" dps do loop é porque n existia a pista com esse id
        return False, "Pista não encontrada"


    tracks.remove(found_tracks)                                                                     #Remove a pista encontrada da lista de pistas


    with open("Entidades/Pista/pista.json", "w", encoding="utf-8") as file:                          #Abre o mesmo arquivo, agora em modo escrita, o que sobrescreve o conteúdo antigo.
        json.dump(tracks, file, indent=4, ensure_ascii=False)                                        #indent=4: deixa o JSON formatado com identação, mais legível. 
                                                                                                        #ensure_ascii=False: mantém acentos e caracteres especiais como estão       
    return True, "Pista removida com sucesso"   