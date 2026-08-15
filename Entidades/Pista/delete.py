import json


def delete(id_pista):
    try:
        with open("Entidades/Pista/pista.json", "r", encoding="utf-8") as arquivo:                      #Abre o arquivo.
            pistas = json.load(arquivo)                                                                 #pega o conteúdo do arquivo e transforma em um objeto Python
    except:
        return False, "Erro ao acessar a base de dados de pistas"                                       #Erro caso não encontre a pista



    pista_encontrada = None
    for pista in pistas:
        if pista["id"] == id_pista:                                                                     #Se o id da pista for igual ao encontrado, guarda essa pista
            pista_encontrada = pista
            break



    if pista_encontrada is None:                                                                        #Caso a pista_encontrada continue "none" dps do loop é porque n existia a pista com esse id
        return False, "Pista não encontrada"


    pistas.remove(pista_encontrada)                                                                     #Remove a pista encontrada da lista de pistas


    with open("Entidades/Pista/pista.json", "w", encoding="utf-8") as arquivo:                          #Abre o mesmo arquivo, agora em modo escrita, o que sobrescreve o conteúdo antigo.
        json.dump(pistas, arquivo, indent=4, ensure_ascii=False)                                        #indent=4: deixa o JSON formatado com identação, mais legível. 
                                                                                                        #ensure_ascii=False: mantém acentos e caracteres especiais como estão       
    return True, "Pista removida com sucesso"   