
import pygame
from pygame.locals import *
import sys

from Jogo.tela_game_over import tela_game_over
from Jogo.jogo import tela_inicial
from Jogo.jogo import tela_ranking

# from Jogo.tela_ranking import tela_ranking

import Jogo.get_images as get_images


pygame.init()

# Definindo tela
LARGURA, ALTURA = 500, 700
TELA = pygame.display.set_mode((LARGURA, ALTURA))

L_CARRO, A_CARRO = 40, 55

pygame.display.set_caption("Corrida Arcade")

# Taxa de frames
RELOGIO = pygame.time.Clock()
FPS = 60


# Pista padrão
PISTA_DEFAULT = {
    "id": 1,
    "nome": "mudei o nome 2",
    "is_public": True,
    "tipo_de_relevo": "Campos verdes",
    "velocidade": 1,
    "quantidade_obstaculos": 1,
    "melhor_desempenho": 1000,
    "jogador_de_melhor_desempenho": "teste1", 
    "carro": "azul"
}


# Loop principal
def tela_principal( pista=PISTA_DEFAULT ):
    running = True

    tela_inicial(TELA)

    bgs_pista = get_images.get_bg_pista(pista["tipo_de_relevo"])
    carro = get_images.get_carro(pista["carro"])
    obstaculos = get_images.get_obstaculos(pista["quantidade_obstaculos"])

    # Imagens
    # --- Pista
    BG_IMAGE1 = pygame.image.load(bgs_pista[0]).convert()
    BG_IMAGE1 = pygame.transform.scale(BG_IMAGE1, (LARGURA, ALTURA))

    BG_IMAGE2 = pygame.image.load(bgs_pista[1]).convert()
    BG_IMAGE2 = pygame.transform.scale(BG_IMAGE2, (LARGURA, ALTURA))

    # --- Carro
    CARRO_PLAYER = pygame.image.load(carro).convert_alpha() # Mantém fundo transparente
    CARRO_PLAYER = pygame.transform.scale(CARRO_PLAYER, (L_CARRO, A_CARRO))


    # Velocidade
    velocidade = 2

    # Posições
    Y_PISTA_1 = 0
    Y_PISTA_2 = -ALTURA

    XY_CARRO_PLAYER = [LARGURA//2, ALTURA-100]
    
    while running:
        velocidade += 0.0001
        TELA.blit(BG_IMAGE1, (0,Y_PISTA_1))
        TELA.blit(BG_IMAGE2, (0,Y_PISTA_2))

        Y_PISTA_1 += velocidade
        Y_PISTA_2 += velocidade

        # Loop infinito da pista
        if Y_PISTA_1 >= ALTURA:
            Y_PISTA_1 = - ALTURA

        if Y_PISTA_2 >= ALTURA:
            Y_PISTA_2 = - ALTURA

        # Eventos de entrada
        for event in pygame.event.get():
            # Encerrar o jogo
            if event.type == pygame.QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_KP_ENTER or event.key == K_RETURN:
                    res = tela_game_over(tela=TELA, melhor_pontuacao="1000", pontuacao="dehrfke", tempo_total=1000)

                    while res != "jogar_novamente" and res != "sair":
                        # tela_ranking(TELA, "jfijowaof", 1000)
                        tela_ranking(TELA)
                        res = tela_game_over(tela=TELA, melhor_pontuacao="1000", pontuacao="dehrfke", tempo_total=1000)

                    match res:
                        case "jogar_novamente":
                            # Função para reiniciar a corrida
                            pass
                        case "sair":
                            tela_inicial(TELA)

        teclas =  pygame.key.get_pressed()
        if teclas[K_a] or teclas[K_LEFT]:      # Movimenta o player para a esquerda
            if XY_CARRO_PLAYER[0] > 150:
                XY_CARRO_PLAYER[0] -= velocidade 

        if teclas[K_d] or teclas[K_RIGHT]:      # Movimenta o player para a direita
            if XY_CARRO_PLAYER[0] < 360:
                XY_CARRO_PLAYER[0] += velocidade 

        CARRO_PLAYER_RECT = CARRO_PLAYER.get_rect(center=XY_CARRO_PLAYER)

        TELA.blit(CARRO_PLAYER, CARRO_PLAYER_RECT)


        pygame.display.flip()

        RELOGIO.tick(FPS)


    pygame.quit()
    sys.exit()

