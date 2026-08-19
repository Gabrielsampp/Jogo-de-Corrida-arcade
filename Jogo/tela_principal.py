
import pygame
from pygame.locals import *
from random import randint
from random import choice
from datetime import datetime
from pathlib import Path
import sys

from Jogo.tela_game_over import tela_game_over
# from Jogo.jogo import tela_inicial
# from Jogo.jogo import tela_ranking

from Jogo.tela_inicial import tela_inicial
from Jogo.tela_ranking import tela_ranking

import Jogo.get_images as get_images
from Entidades.Pista.update import update as pista_update


# Definindo tela
LARGURA, ALTURA = 500, 700

L_CARRO, A_CARRO = 40, 55


# Pista padrão
PISTA_DEFAULT = {
    "id": 2,
    "name": "mudei o nome 2",
    "is_public": True,
    "landform": "Campos verdes",
    "speed": 3,
    "obstacles": 10,
    "best_performance": 0,
    "best_performance_player": "teste1",
    "car": "azul"
}


# Funções auxiliares

# Loop principal

def tela_principal( pista=PISTA_DEFAULT, jogador="teste1" ):
    
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    # Músicas e efeitos sonoros
    FIM_DA_MUSICA = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(FIM_DA_MUSICA)

    BASEDIR = Path(__file__).parent.parent / "Musicas"

    MUSICAS_DE_FUNDO = [
        BASEDIR / "back_music1.mp3",
        BASEDIR / "back_music2.mpeg",
        BASEDIR / "sound_teste.mp3",
    ]

    pygame.mixer.music.load( BASEDIR / "game_over.mp3" )
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

    def next_music():
        pygame.mixer.music.load( choice(MUSICAS_DE_FUNDO) )
        pygame.mixer.music.play()



    end_game = pygame.mixer.Sound( BASEDIR / "faaah.mp3" )
    end_game.set_volume(0.8)


    FONTE = pygame.font.SysFont("couriernew", 30, bold=True)
    TELA = pygame.display.set_mode((LARGURA, ALTURA))

    app = tela_inicial(TELA)
    if app == "sair":
        return

    MOMENTO_INICIAL = datetime.now()
    pygame.mixer.music.stop()
    pygame.mixer.music.load( MUSICAS_DE_FUNDO[0] )
    pygame.mixer.music.play()

    pygame.display.set_caption("Corrida Arcade")

    # Taxa de frames
    RELOGIO = pygame.time.Clock()
    FPS = 60

    # Buscando informações da pista
    bgs_pista = get_images.get_bg_pista(pista["landform"])
    carro = get_images.get_carro(pista["car"])
    obstaculos_paths = get_images.get_obstaculos(pista["obstacles"])
    quadro_pontos_path = get_images.get_quadro_pontos()
    
    # Velocidade
    velocidade = pista["speed"]

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

    # Posições
    Y_PISTA_1 = 0
    Y_PISTA_2 = -ALTURA

    BORDA_ESQUERDA = 130
    BORDA_DIREITA = 340

    XY_CARRO_PLAYER = [LARGURA//2, ALTURA-100]
    CARRO_PLAYER_RECT = CARRO_PLAYER.get_rect(center=XY_CARRO_PLAYER)


    # Obstáculos
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
            obstaculo["rect"] = image.get_rect(center=(randint(BORDA_ESQUERDA, BORDA_DIREITA), OBSTACULOS[-1]["rect"].y-200))
            OBSTACULOS.append(obstaculo)

        return OBSTACULOS


    OBSTACULOS = listar_obstaculos(obstaculos_paths, BORDA_ESQUERDA, BORDA_DIREITA)

    running = True
    PONTOS = 0

    def reiniciar(obstaculos_paths):
        velocidade = pista["speed"]
        Y_PISTA_1 = 0
        Y_PISTA_2 = -ALTURA
        CARRO_PLAYER_RECT.x = LARGURA//2
        CARRO_PLAYER_RECT.y = ALTURA - 100
        PONTOS = 0    
        OBSTACULOS = listar_obstaculos(obstaculos_paths, BORDA_ESQUERDA, BORDA_DIREITA)
        MOMENTO_INICIAL = datetime.now()

        pygame.mixer.music.stop()
        next_music()

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

                PONTOS += 1 + pista["obstacles"] // 5


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

            if event.type == FIM_DA_MUSICA:
                next_music()

        teclas =  pygame.key.get_pressed()
        # Movimentação horizontal
        if teclas[K_a] or teclas[K_LEFT]:      # Movimenta o player para a esquerda
            if CARRO_PLAYER_RECT.x > BORDA_ESQUERDA:
                CARRO_PLAYER_RECT.x -= velocidade 

        if teclas[K_d] or teclas[K_RIGHT]:      # Movimenta o player para a direita
            if CARRO_PLAYER_RECT.x < BORDA_DIREITA:
                CARRO_PLAYER_RECT.x += velocidade 

        # Movimentação vertical
        if teclas[K_w] or teclas[K_UP]:      # Movimenta o player para cima
            if CARRO_PLAYER_RECT.y > 0:
                CARRO_PLAYER_RECT.y -= velocidade 

        if teclas[K_s] or teclas[K_DOWN]:      # Movimenta o player para baixo
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
                end_game.play()
                if int(pista["best_performance"]) < PONTOS:
                    if jogador == pista["best_performance_player"]:
                        pista_update(pista["id"], { "best_performance": PONTOS, "best_performance_player": jogador} )

                    elif jogador != pista["best_performance_player"] and pista["is_public"]:
                        pista_update(pista["id"], { "best_performance": PONTOS, "best_performance_player": jogador} )
                    

                MOMENTO_FINAL = datetime.now()

                diferenca = MOMENTO_FINAL - MOMENTO_INICIAL

                tempo_total = diferenca.total_seconds()


                pygame.mixer.music.stop()
                pygame.mixer.music.load(BASEDIR / "game_over.mp3")
                pygame.mixer.music.play()
                res = tela_game_over(tela=TELA, melhor_pontuacao=pista["best_performance"], pontuacao=PONTOS, tempo_total=tempo_total)
                CARRO_PLAYER_RECT.x == LARGURA // 2
                CARRO_PLAYER_RECT.y == ALTURA - 100

                while res != "jogar_novamente" and res != "sair":
                    app = tela_ranking(TELA, jogador=jogador, resultado=PONTOS)
                    if app == "sair":
                        return
                    # tela_ranking(TELA)
                    res = tela_game_over(tela=TELA, melhor_pontuacao=pista["best_performance"], pontuacao=PONTOS, tempo_total=1000)

                match res:
                    case "jogar_novamente":
                        velocidade, Y_PISTA_1, Y_PISTA_2, PONTOS, OBSTACULOS, MOMENTO_INICIAL = reiniciar(obstaculos_paths)
                        
                    case "sair":
                        app = tela_inicial(TELA)
                        if app == "sair":
                            return
                        velocidade, Y_PISTA_1, Y_PISTA_2, PONTOS, OBSTACULOS, MOMENTO_INICIAL = reiniciar(obstaculos_paths)
                    

        pygame.display.flip()

        RELOGIO.tick(FPS)


    pygame.quit()

