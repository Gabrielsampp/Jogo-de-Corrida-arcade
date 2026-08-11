from Entidades.Pista.get_publics import get_publics

pistas = get_publics()
##############Abaixo segue o modelo de separação de informações de cada pista, para que fique mais fácil de visualizar os dados.##############
##############Modelo pode ser utilizado posteriormente para exibir as informações de cada pista e também dos jogadores, caso seja necessário.##############
for pista in pistas:
    print(f"ID: {pista['id']}")
    print(f"Nome: {pista['nome']}")
    print(f"Relevo: {pista['tipo_de_relevo']}")
    print(f"Velocidade: {pista['velocidade']}")
    print(f"Obstáculos: {pista['quantidade_obstaculos']}")
    print(f"Melhor desempenho: {pista['melhor_desempenho']}")
    print(f"Jogador: {pista['jogador_de_melhor_desempenho']}")
    print("-" * 30)    # separador visual
    print()            # quebra de linha em branco