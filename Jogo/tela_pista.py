import pygame
import sys 

def coletar_dados_terminal():
    """Coleta as entradas iniciais obrigatórias via console."""
    print("\n--- CONFIGURAÇÃO DA PISTA via TERMINAL ---")
    name = input("Digite o name da pista: ").strip()
    
    while True:
        try:
            speed = float(input("Defina a velocidade (2 á 5 ): "))
            if speed < 2 or speed > 5:
                print("Velocidade deve estar entre 2 e 5.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número decimal entre 2 e 5.")
        
            
    while True:
        try:
            obstacles = int(input("Defina a quantidade de obstáculos ( 5 á 10 ): "))
            if obstacles < 5 or obstacles > 10:
                print("A quantidade de obstáculos deve estar entre 5 e 10.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
        
            
    return name, speed, obstacles


def tela_pista(create):
    """
    Função da interface gráfica.
    Recebe por parâmetro a função de cadastro externa através do argumento 'create'.
    """
    # 1. Armazena os dados textuais recebidos do terminal
    name_pista, speed, obstacles = coletar_dados_terminal()

 # Inicializa o mixer de áudio do Pygame
    pygame.mixer.init()
    pygame.mixer.Sound("Musicas/back_music1.mp3").play()
    
    # 2. Inicialização do ambiente gráfico
    pygame.init()
    LARGURA, ALTURA = 500, 700
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

    # 4. Mapeamento dos retângulos invisíveis de colisão
    # As coordenadas originais foram desenhadas para uma imagem de 576x1024;
    # aqui são reescaladas proporcionalmente para a resolução atual (500x700).
    ESCALA_X = LARGURA / 576
    ESCALA_Y = ALTURA / 1024

    def rect_escalado(x, y, w, h):
        return pygame.Rect(
            round(x * ESCALA_X),
            round(y * ESCALA_Y),
            round(w * ESCALA_X),
            round(h * ESCALA_Y)
        )

    botoes_carros = {
        "roxo":     rect_escalado(62,  140,  80, 128),
        "azul":     rect_escalado(157, 140,  80, 128),
        "verde":    rect_escalado(248, 140,  80, 128),
        "amarelo":  rect_escalado(339, 140,  80, 128),
        "vermelho": rect_escalado(432, 140,  80, 128)
    }

    botoes_pistas = {
        "Campos verdes": rect_escalado(72, 285, 432, 138),  # Faixa Pista 1
        "deserto":       rect_escalado(72, 430, 432, 138),  # Faixa Pista 2
        "antártida":     rect_escalado(72, 573, 432, 138),  # Faixa Pista 3
        "asfalto":       rect_escalado(72, 718, 432, 138)   # Faixa Pista 4
    }

    btn_publica = rect_escalado(97,  870, 180, 45)
    btn_privada = rect_escalado(298, 870, 180, 45)
    btn_criar_sala = rect_escalado(95, 932, 385, 60)

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
                        # Executa a função passada por parâmetro (create)
                        sucesso, mensagem = create(
                            player="teste",
                            name=name_pista,
                            is_public=sala_publica,
                            landform=relevo_selecionada, 
                            speed=speed,
                            obstacles=obstacles,
                            color=cor_selecionada
                        )
                        print(f"\n {mensagem}")
                        
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

if __name__ == "__main__":
    def create_teste(**kwargs):
        print("Dados recebidos:", kwargs)
        return True, "Sala criada com sucesso (teste)"

    tela_pista(create_teste)