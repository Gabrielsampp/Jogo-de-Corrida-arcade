from Entidades.Jogador.get_all import get_all

jogadores = get_all()
##############Abaixo segue o modelo de separação de informações de cada jogador, para que fique mais fácil de visualizar os dados.##############
##############Modelo pode ser utilizado posteriormente para exibir as informações de cada jogador, caso seja necessário.##############
for jogador in jogadores:
    print(f"nickname: {jogador['nickname']}")
    print(f"senha: {jogador['senha']}")
    print()