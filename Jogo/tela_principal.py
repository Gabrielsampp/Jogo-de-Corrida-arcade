
import pygame
from pygame.locals import *
from random import randint
from datetime import datetime
import sys

from Jogo.tela_game_over import tela_game_over
from Jogo.jogo import tela_inicial
from Jogo.jogo import tela_ranking

# from Jogo.tela_ranking import tela_ranking

import Jogo.get_images as get_images
from Entidades.Pista.update import update as pista_update

pygame.init()
pygame.font.init()

FONTE = pygame.font.SysFont("couriernew", 30, bold=True)

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
    "tipo_de_relevo": "antártida",
    "velocidade": 1,
    "quantidade_obstaculos": 7,
    "melhor_desempenho": 0,
    "jogador_de_melhor_desempenho": "teste1", 
    "carro": "azul"
}


# Funções auxiliares

def listar_obstaculos(obstaculos_paths, BORDA_ESQUERDA, BORDA_DIREITA):
    OBSTACULOS = []
    obstaculo = {}

    image = pygame.image.load(obstaculos_paths[0]).convert_alpha()
    image = pygame.transform.scale(image, (L_CARRO, A_CARRO))

    obstaculo["image"] = image
    obstaculo["rect"] = image.get_rect(center=(randint(BORDA_ESQUERDA, BORDA_DIREITA), -50))

    OBSTACULOS.append(obstaculo)

    for obs in obstaculos_paths[1:]:
        obstaculo = {}
        image = pygame.image.load(obs).convert_alpha()
        image = pygame.transform.scale(image, (L_CARRO, A_CARRO))

        obstaculo["image"] = image
        obstaculo["rect"] = image.get_rect(center=(randint(BORDA_ESQUERDA, BORDA_DIREITA), OBSTACULOS[-1]["rect"].y-180))
        OBSTACULOS.append(obstaculo)

    return OBSTACULOS


def tela_principal( pista=PISTA_DEFAULT, jogador="teste1" ):

    tela_inicial(TELA)
    MOMENTO_INICIAL = datetime.now()

    bgs_pista = get_images.get_bg_pista(pista["tipo_de_relevo"])
    carro = get_images.get_carro(pista["carro"])
    obstaculos_paths = get_images.get_obstaculos(pista["quantidade_obstaculos"])
    quadro_pontos_path = get_images.get_quadro_pontos()

    # Imagens
    # --- Pista
    BG_IMAGE1 = pygame.image.load(bgs_pista[0]).convert()
    BG_IMAGE1 = pygame.transform.scale(BG_IMAGE1, (LARGURA, ALTURA))

    BG_IMAGE2 = pygame.image.load(bgs_pista[1]).convert()
    BG_IMAGE2 = pygame.transform.scale(BG_IMAGE2, (LARGURA, ALTURA))

    # --- Carro
    CARRO_PLAYER = pygame.image.load(carro).convert_alpha() # Mantém fundo transparente
    CARRO_PLAYER = pygame.transform.scale(CARRO_PLAYER, (L_CARRO, A_CARRO))

    # --- Quadro pontos
    QUADRO_PONTOS = pygame.image.load(quadro_pontos_path).convert_alpha()
    QUADRO_PONTOS = pygame.transform.scale(QUADRO_PONTOS, (LARGURA, 80))
    QUADRO_PONTOS_RECT = QUADRO_PONTOS.get_rect()

    # Velocidade
    velocidade = 3

    # Posições
    Y_PISTA_1 = 0
    Y_PISTA_2 = -ALTURA

    BORDA_ESQUERDA = 130
    BORDA_DIREITA = 340

    XY_CARRO_PLAYER = [LARGURA//2, ALTURA-100]
    CARRO_PLAYER_RECT = CARRO_PLAYER.get_rect(center=XY_CARRO_PLAYER)


    # Obstáculos
    OBSTACULOS = listar_obstaculos(obstaculos_paths, BORDA_ESQUERDA, BORDA_DIREITA)

    running = True
    PONTOS = 0

    def reiniciar(obstaculos_paths):
        velocidade = 3
        Y_PISTA_1 = 0
        Y_PISTA_2 = -ALTURA
        CARRO_PLAYER_RECT.x = LARGURA//2
        CARRO_PLAYER_RECT.y = ALTURA - 100
        PONTOS = 0    
        OBSTACULOS = listar_obstaculos(obstaculos_paths, BORDA_ESQUERDA, BORDA_DIREITA)
        MOMENTO_INICIAL = datetime.now()

        return velocidade, Y_PISTA_1, Y_PISTA_2, PONTOS, OBSTACULOS, MOMENTO_INICIAL

    while running:
        velocidade += 0.001

        TELA.blit(BG_IMAGE1, (0,Y_PISTA_1))
        TELA.blit(BG_IMAGE2, (0,Y_PISTA_2))

        Y_PISTA_1 += velocidade
        Y_PISTA_2 += velocidade


        # Texto:
        texto_pontos = FONTE.render(f"{PONTOS}", True, (255, 255, 255))


        # Loop infinito dos obstáculos
        for obs in OBSTACULOS:
            obs["rect"].y += velocidade

            if obs["rect"].y >= ALTURA:
                obs["rect"].y = -180
                obs["rect"].x = randint(BORDA_ESQUERDA, BORDA_DIREITA)

                PONTOS += 1 + pista["quantidade_obstaculos"] // 5


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

        teclas =  pygame.key.get_pressed()
        # Movimentação horizontal
        if teclas[K_a] or teclas[K_LEFT]:      # Movimenta o player para a esquerda
            if CARRO_PLAYER_RECT.x > BORDA_ESQUERDA:
                CARRO_PLAYER_RECT.x -= velocidade 

        if teclas[K_d] or teclas[K_RIGHT]:      # Movimenta o player para a direita
            if CARRO_PLAYER_RECT.x < BORDA_DIREITA:
                CARRO_PLAYER_RECT.x += velocidade 

        # Movimentação vertical
        if teclas[K_w] or teclas[K_UP]:      # Movimenta o player para a esquerda
            if CARRO_PLAYER_RECT.y > 0:
                CARRO_PLAYER_RECT.y -= velocidade 

        if teclas[K_s] or teclas[K_DOWN]:      # Movimenta o player para a direita
            if CARRO_PLAYER_RECT.y < ALTURA - A_CARRO:
                CARRO_PLAYER_RECT.y += velocidade 


        # Player na tela
        TELA.blit(CARRO_PLAYER, CARRO_PLAYER_RECT)


        # Obstáculos na tela
        for obs in OBSTACULOS:
            TELA.blit(obs["image"], obs["rect"])


        # Quadro pontos na tela
        TELA.blit(QUADRO_PONTOS, (0,0))
        TELA.blit(texto_pontos, ( LARGURA - 170, QUADRO_PONTOS_RECT.height // 2 - 14))


        # Colisões entre carros
        for obs in OBSTACULOS:
            if CARRO_PLAYER_RECT.colliderect(obs["rect"]):

                if pista["melhor_desempenho"] < PONTOS:
                    if jogador == pista["jogador_de_melhor_desempenho"]:
                        pista_update(pista["id"], { "melhor_desempenho": PONTOS, "jogador_de_melhor_desempenho": jogador} )

                    elif jogador != pista["jogador_de_melhor_desempenho"] and pista["is_public"]:
                        pista_update(pista["id"], { "melhor_desempenho": PONTOS, "jogador_de_melhor_desempenho": jogador} )
                    

                MOMENTO_FINAL = datetime.now()

                diferenca = MOMENTO_FINAL - MOMENTO_INICIAL

                tempo_total = diferenca.total_seconds()

                res = tela_game_over(tela=TELA, melhor_pontuacao="1000", pontuacao=PONTOS, tempo_total=tempo_total)
                

                while res != "jogar_novamente" and res != "sair":
                    # tela_ranking(TELA, "jfijowaof", 1000)
                    tela_ranking(TELA)
                    res = tela_game_over(tela=TELA, melhor_pontuacao="1000", pontuacao=PONTOS, tempo_total=1000)

                match res:
                    case "jogar_novamente":
                        velocidade, Y_PISTA_1, Y_PISTA_2, PONTOS, OBSTACULOS, MOMENTO_INICIAL = reiniciar(obstaculos_paths)
                        
                    case "sair":
                        tela_inicial(TELA)
                        velocidade, Y_PISTA_1, Y_PISTA_2, PONTOS, OBSTACULOS, MOMENTO_INICIAL = reiniciar(obstaculos_paths)
                    

        pygame.display.flip()

        RELOGIO.tick(FPS)


    pygame.quit()
    sys.exit()

