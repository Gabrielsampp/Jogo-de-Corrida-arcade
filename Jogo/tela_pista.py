import pygame

def coletar_dados_terminal():
    """Coleta as entradas iniciais obrigatórias via console."""
    print("\n--- CONFIGURAÇÃO DA PISTA via TERMINAL ---")
    nome = input("Digite o nome da pista: ").strip()
    
    while True:
        try:
            velocidade = float(input("Digite a velocidade (float): "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número decimal.")
            
    while True:
        try:
            obstaculos = int(input("Digite a quantidade de obstáculos (int): "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            
    return nome, velocidade, obstaculos


def tela_pista(create):
    """
    Função da interface gráfica.
    Recebe por parâmetro a função de cadastro externa através do argumento 'create'.
    """
    # 1. Armazena os dados textuais recebidos do terminal
    nome_pista, velocidade, obstaculos = coletar_dados_terminal()

    # 2. Inicialização do ambiente gráfico
    pygame.init()
    LARGURA, ALTURA = 576, 1024
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Selecionar Pista")
    
    # Carrega a imagem enviada como plano de fundo
    try:
        fundo = pygame.image.load("Imagens/tela_pista.png")
        fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))
    except FileNotFoundError:
        print("Erro crítico: Arquivo 'tela_pista.png' não encontrado no diretório.")
        pygame.quit()
        sys.exit()

    # 3. Variáveis de Estado internas para as seleções visuais
    cor_selecionada = None          # Receberá a string da cor do carro selecionado
    relevo_selecionada = None       # Receberá a string do tipo de relevo selecionado
    sala_publica = True            # Controle lógico: Pública (True) ou Privada (False)

    # 4. Mapeamento dos retângulos invisíveis de colisão (Layout exato da imagem)
    botoes_carros = {
        "roxo":     pygame.Rect(75,  140,  70, 115),
        "azul":     pygame.Rect(155, 140,  70, 115),
        "verde":    pygame.Rect(238, 140,  70, 115),
        "amarelo":  pygame.Rect(320, 140,  70, 115),
        "vermelho": pygame.Rect(402, 140,  70, 115)
    }

    botoes_pistas = {
        "Campos verdes": pygame.Rect(72, 280, 432, 138),  # Faixa Pista 1
        "deserto":       pygame.Rect(72, 426, 432, 138),  # Faixa Pista 2
        "antártida":     pygame.Rect(72, 572, 432, 138),  # Faixa Pista 3
        "asfalto":       pygame.Rect(72, 718, 432, 138)   # Faixa Pista 4
    }

    btn_publica = pygame.Rect(95,  865, 180, 45)
    btn_privada = pygame.Rect(298, 865, 180, 45)
    btn_criar_sala = pygame.Rect(95, 922, 385, 60)

    # Configuração visual das bordas vazadas (Cores em RGB)
    COR_HOVER = (0, 255, 255)       # Ciano quando passa o mouse por cima
    COR_FIXA = (255, 215, 0)        # Dourado para fixar o item atualmente selecionado

    clock = pygame.time.Clock()
    rodando = True

    # Loop Principal da Janela
    while rodando:
        mouse_pos = pygame.mouse.get_pos()
        
        # Limpa o frame desenhando a imagem de fundo nativa
        tela.blit(fundo, (0, 0))

        # --- MONITORAMENTO DE EVENTOS DA INTERFACE ---
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                # Verificação de clique nos carros
                for cor, rect in botoes_carros.items():
                    if rect.collidepoint(evento.pos):
                        cor_selecionada = cor

                # Verificação de clique nos blocos de pista
                for relevo, rect in botoes_pistas.items():
                    if rect.collidepoint(evento.pos):
                        relevo_selecionada = relevo

                # Verificação de clique nas opções de privacidade
                if btn_publica.collidepoint(evento.pos):
                    sala_publica = True
                elif btn_privada.collidepoint(evento.pos):
                    sala_publica = False

                # Execução e envio de dados pelo botão invisível "CRIAR SALA"
                if btn_criar_sala.collidepoint(evento.pos):
                    if cor_selecionada is None:
                        print("Aviso: Selecione um carro antes de continuar.")
                    elif relevo_selecionada is None:
                        print("Aviso: Selecione uma pista antes de continuar.")
                    else:
                        # Executa a função passada por parâmetro (seu create)
                        sucesso, mensagem = create(
                            nome=nome_pista,
                            is_public=sala_publica,
                            tipo_relevo=[relevo_selecionada], # Converte para lista conforme seu JSON espera
                            velocidade=velocidade,
                            qtd_obstaculos=obstaculos,
                            cor=cor_selecionada
                        )
                        print(f"\n[Retorno do JSON]: {mensagem}")
                        
                        # Se gravou com sucesso, encerra a interface gráfica
                        if sucesso:
                            rodando = False

        # --- PROCESSAMENTO EXCLUSIVO DE CONTORNOS/BORDAS (Apenas linhas vazadas) ---
        
        # Contorno dos Carros
        for cor, rect in botoes_carros.items():
            if cor_selecionada == cor:
                pygame.draw.rect(tela, COR_FIXA, rect, width=4, border_radius=8)
            elif rect.collidepoint(mouse_pos):
                pygame.draw.rect(tela, COR_HOVER, rect, width=4, border_radius=8)

        # Contorno das Pistas
        for relevo, rect in botoes_pistas.items():
            if relevo_selecionada == relevo:
                pygame.draw.rect(tela, COR_FIXA, rect, width=4, border_radius=12)
            elif rect.collidepoint(mouse_pos):
                pygame.draw.rect(tela, COR_HOVER, rect, width=4, border_radius=12)

        # Contorno do modo de Privacidade
        if sala_publica:
            pygame.draw.rect(tela, COR_FIXA, btn_publica, width=4, border_radius=6)
            if btn_privada.collidepoint(mouse_pos):
                pygame.draw.rect(tela, COR_HOVER, btn_privada, width=4, border_radius=6)
        else:
            pygame.draw.rect(tela, COR_FIXA, btn_privada, width=4, border_radius=6)
            if btn_publica.collidepoint(mouse_pos):
                pygame.draw.rect(tela, COR_HOVER, btn_publica, width=4, border_radius=6)

        # Contorno de destaque ao passar o mouse no botão "CRIAR SALA"
        if btn_criar_sala.collidepoint(mouse_pos):
            pygame.draw.rect(tela, COR_HOVER, btn_criar_sala, width=4, border_radius=10)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
