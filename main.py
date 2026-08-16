from Jogo.tela_principal import tela_principal as jogo

while True:
    try:
        jogo()
        res = input()
        
        if res != "":
            break

    except Exception as e:
        print(str(e))
        break 
