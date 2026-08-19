# TELA RANKING - PONTUAÇÃO

import pygame
import sys

from Entidades.Ranking.get_all import get_all
from Entidades.Ranking.update import update

def tela_ranking(tela, jogador, resultado): #       FUNÇÃO PRINCIPAL
    running = True
    pygame.init()
    #                                               TAMANHO DA TELA
    LARGURA = 500
    ALTURA = 700

    BG_INIT = pygame.image.load("Imagens/tela_ranking.png").convert()
    BG_INIT = pygame.transform.scale(BG_INIT, (LARGURA, ALTURA))
    
    fonte_titulo = pygame.font.Font(None, 30)
    fonte = pygame.font.Font(None, 22)
    relogio = pygame.time.Clock() # Limita o FPS

    def carregar_top10():         # Limita o Ranking para 10 jogadores
        lista = get_all()
        return lista[:10]
      
    ranking = carregar_top10()    # lista do ranking               

    #                                               ELEMENTO ESTÁTICOS
    # Textos 
    texto_titulo = fonte_titulo.render("RANKING - TOP 10", True, (255, 255, 255))
    texto_resultado = fonte_titulo.render(f"Seu resultado: {resultado}", True, (255, 255, 0))
    texto_adicionar = fonte.render("ADICIONAR AO RANKING", True, (255, 255, 255))
    texto_voltar = fonte.render("VOLTAR", True, (255, 255, 255))

    # Retângulos dos botões
    area_botao_adicionar = pygame.Rect(100, 570, 300, 50)
    area_botao_voltar = pygame.Rect(175, 630, 150, 45)

    #                                               LAÇO DE EVENTOS
    pontuacao_ja_salva = False  # evita trapaças
    while True:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return "sair"
                # sys.exit()
            
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: # registro de clique no botão esquedro

                # Clique no Botão Adicionar Pontuação
                if area_botao_adicionar.collidepoint(evento.pos) and not pontuacao_ja_salva:
                    id_alvo = jogador.get("id") if isinstance(jogador, dict) else jogador
                    sucesso, mensagem = update(jogador, resultado)

                    if sucesso:
                        ranking = carregar_top10()
                        pontuacao_ja_salva = True
                    else:
                        print(f"Erro ao salvar: {mensagem}")

                # Clique no Botão Voltar
                if area_botao_voltar.collidepoint(evento.pos):
                    return "game_over"
                
         #                                           ELEMENTOS NA TELA
        tela.blit(BG_INIT, (0, 0))

        # Título e Resultado do Jogador
        tela.blit(
            texto_titulo,
            texto_titulo.get_rect(center=(LARGURA // 2, 115))
        )

        tela.blit(
            texto_resultado,
            texto_resultado.get_rect(center=(LARGURA // 2, 550))
        )

        # Lista do Top 10 Jogadores
        for i, jogador_ranking in enumerate(ranking):
            texto_jogador = fonte.render(
                f"{i + 1}º - {jogador_ranking['nickname']} {"- "*(44 - len(jogador_ranking["nickname"]) - len(str(jogador_ranking['score'])))}- {jogador_ranking['score']}",
                # "- "*49,
                True,
                (255, 255, 255)
            )

            tela.blit(
                texto_jogador,
                texto_jogador.get_rect(center=(LARGURA // 2, 190 + i * 34))
            )

        # Botão Adicionar - Verde por padrão | Cinza se clicado
        cor_botao_adicionar = (100, 100, 100) if pontuacao_ja_salva else (0, 150, 0)

        pygame.draw.rect(
            tela,
            cor_botao_adicionar,
            area_botao_adicionar
        )

        tela.blit(
            texto_adicionar,
            texto_adicionar.get_rect(center=area_botao_adicionar.center)
        )

        # Botão Voltar
        pygame.draw.rect(
            tela,
            (150, 0, 0),
            area_botao_voltar
        )

        tela.blit(
            texto_voltar,
            texto_voltar.get_rect(center=area_botao_voltar.center)
        )

        pygame.display.flip()

        relogio.tick(60)