
from Entidades.Jogador import jogador
from Entidades.Pista import pista
from Entidades.Admin import admin
from Entidades.Ranking import ranking


# Testes

try:
    '''Jogador
    assert jogador.update(nickname="teste2", new_data={ "password": "1234" }) == True, "Jogador/update"
    assert jogador.create(nickname="jogador1", password="123") == "Jogador criado com sucesso!", "Jogador/create" # Tem que ajustar a saída dessa função (bool, str)
    assert jogador.delete(nickname="jogador1") == "Jogador removido", "Jogador/delete"      # Tem que ajustar a saída (bool, str)
    assert isinstance(jogador.get_all(), list) and len(jogador.get_all()) > 0, "Jogador/get_all"
    assert jogador.get_by_username(nickname="teste1")["nickname"] == "teste1", "Jogador/get_by_username"
    assert jogador.login(nickname="teste1", password="123")[0] == True, "Jogador/login"
    
    print("Tudo certo")'''
except AssertionError as e:
    print(str(e))

except Exception as e:
    print(str(e))


try:
    '''Admin
    assert admin.update(new_data={"password": "admin1234"})[0] == True, "Admin/update"                                   # Tem que implementar pathlib
    assert admin.get()["username"] == "admin", "Admin/get"
    assert admin.login(username="admin", password="admin1234") == True, "Admin/login"
    
    print("Tudo certo")'''
except AssertionError as e:
    print(str(e))

except Exception as e:
    print(str(e))


try:
    '''Pista
    assert len(pista.get_all()) > 0, "Pista/get_all"   # Adicionar tratamento de erro caso o json esteja vazio
    assert pista.create(name="testePista", is_public=True, landform="asfalto", speed=3, obstacles=7, color="azul", player="teste1")[0] == True, "Pista/create"
    assert pista.delete(pista.get_last_id())[0] == True, "Pista/delete and get_last_id"
    assert pista.update(id=1, new_data={"speed": 2})[0] == True, "Pista/update"
    assert len(pista.get_by_list_id(id_list=[1, 2])) > 0, "Pista/get_by_list_id"
    assert len(pista.get_publics()) > 0, "Pista/get_publics"        # implementar pathlib
    
    print("Tudo certo")'''
except AssertionError as e:
    print(e)

except Exception as e:
    print(str(e))



try:
    '''Ranking
    assert ranking.add_player("testeRank1", 150)[0] == True, "Ranking/add_player"
    # assert ranking.delete()[0] == True, "Ranking/delete"
    assert len(ranking.get_all()) > 0, "Ranking/get_all"
    assert ranking.remove_player(nickname="testeRank1")[0] == True
    assert ranking.update(nickname="xXwandersonXx", score=991)
    
    print("Tudo certo")'''
except AssertionError as e:
    print(e)

except Exception:
    print(Exception)


# Erros encontrados