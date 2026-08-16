import pygame
import sys

def tela_inicial(TELA):
    running = True
    pygame.init()

    # 1. Carrega a imagem de fundo
    BG_INIT = pygame.image.load("Imagens/bg-tela-inicial.png").convert()
    BG_INIT = pygame.transform.scale(BG_INIT, (500, 700))

    # 2. Configura a fonte e as áreas (retângulos) dos botões
    fonte = pygame.font.SysFont("Arial", 28, bold=True)
    
    # Criamos os retângulos dos botões: (pos_x, pos_y, largura, altura)
    btn_jogar_rect = pygame.Rect(150, 450, 200, 50)
    btn_sair_rect = pygame.Rect(150, 530, 200, 50)

    # Renderiza os textos dos botões
    txt_jogar = fonte.render("JOGAR", True, (255, 255, 255))
    txt_sair = fonte.render("SAIR", True, (255, 255, 255))

    while running:
        # A. Desenha a imagem de fundo
        TELA.blit(BG_INIT, (0, 0))

        # B. Desenha os botões (retângulos com cor)
        pygame.draw.rect(TELA, (0, 150, 0), btn_jogar_rect)  # Botão Verde (Jogar)
        pygame.draw.rect(TELA, (180, 0, 0), btn_sair_rect)   # Botão Vermelho (Sair)

        # C. Desenha os textos centralizados nos botões
        TELA.blit(txt_jogar, (btn_jogar_rect.x + 55, btn_jogar_rect.y + 10))
        TELA.blit(txt_sair, (btn_sair_rect.x + 65, btn_sair_rect.y + 10))

        # D. Eventos de Entrada
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return "sair"
                # sys.exit()

            # Clique do mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botão esquerdo do mouse
                    pos_mouse = event.pos
                    
                    # Verifica clique no botão Jogar
                    if btn_jogar_rect.collidepoint(pos_mouse):
                        running = False
                    
                    # Verifica clique no botão Sair
                    if btn_sair_rect.collidepoint(pos_mouse):
                        pygame.quit()
                        return "sair"
                        # sys.exit()

            # Tecla ENTER para jogar rápido
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    running = False

        pygame.display.flip()