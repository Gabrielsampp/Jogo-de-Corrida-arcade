
import pygame
import sys
from pygame.locals import *


def tela_inicial(TELA):
    running = True

    BG_INIT = pygame.image.load("Imagens/bg-tela-inicial.png").convert()
    BG_INIT = pygame.transform.scale(BG_INIT, (500, 700))

    while running:
        
        # Eventos de entrada
        for event in pygame.event.get():

            # Encerrar o jogo
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()


            if event.type == KEYDOWN:
                if event.key == K_KP_ENTER or event.key == K_RETURN:
                    running = False

        TELA.blit(BG_INIT, (0,0))
        pygame.display.flip()

        


def tela_ranking(TELA):
    running = True

    BG_RANK = pygame.image.load("Imagens/sprite-sheet-jogo-corrida.jpg").convert()
    BG_RANK = pygame.transform.scale(BG_RANK, (500, 700))

    while running:
        # Eventos de entrada
        for event in pygame.event.get():

            # Encerrar o jogo
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_v:
                    running = False

        TELA.blit(BG_RANK, (0,0))
        pygame.display.flip()
