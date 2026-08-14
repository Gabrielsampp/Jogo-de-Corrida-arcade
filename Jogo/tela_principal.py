
import pygame
from pygame.locals import *
import sys

from Jogo.tela_game_over import tela_game_over
from Jogo.jogo import tela_inicial
from Jogo.jogo import tela_ranking

pygame.init()

# Definindo tela
LARGURA, ALTURA = 500, 700
TELA = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption("Corrida Arcade")

# Taxa de frames
RELOGIO = pygame.time.Clock()
FPS = 60


# Imagens
BG_IMAGE = pygame.image.load("Imagens/pista_campos_verdes_1.png").convert()
BG_IMAGE = pygame.transform.scale(BG_IMAGE, (LARGURA, ALTURA))

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
    # tela_game_over(tela=TELA, melhor_pontuacao="niueriehnv", pontuacao="dehrfke", tempo_total=1000)
    
    
    while running:
        TELA.blit(BG_IMAGE, (0,0))
        

        # Eventos de entrada
        for event in pygame.event.get():
            # Encerrar o jogo
            if event.type == pygame.QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_KP_ENTER or event.key == K_RETURN:
                    res = tela_game_over(tela=TELA, melhor_pontuacao="1000", pontuacao="dehrfke", tempo_total=1000)

                    while res != "jogar_novamente" and res != "sair":
                        tela_ranking(TELA)
                        res = tela_game_over(tela=TELA, melhor_pontuacao="1000", pontuacao="dehrfke", tempo_total=1000)

                    match res:
                        case "jogar_novamente":
                            # Função para reiniciar a corrida
                            pass
                        case "sair":
                            tela_inicial(TELA)

        
        
        # TELA.fill((0,50,0))


        pygame.display.flip()

        RELOGIO.tick(FPS)


    pygame.quit()
    sys.exit()
