# TELA RANKING - PONTUAÇÃO

import pygame

from Entidades.Ranking.get_all import get_all
# from Entidades.Ranking.update import update


def tela_ranking(tela, jogador, resultado): #             FUNÇÃO PRINCIPAL

    # tela = pygame.display.set_mode((800, 600)) 
    fonte = pygame.font.Font(None, 22)
    relogio = pygame.time.Clock() # Limita o FPS

    def carregar_top10():         # Função para carregar e ordenar o ranking
        lista = get_all()
        # lista = dados.get("ranking", [])
        # lista.sort(key=lambda jogador: jogador["pontuação"], reverse=True)
        return lista[:10]
      
    ranking = carregar_top10()    # lista do ranking               

    #                                               ELEMENTO ESTÁTICOS
    # Textos 
    texto_titulo = fonte.render("RANKING - TOP 10", True, (255, 255, 255))
    texto_resultado = fonte.render(f"Seu resultado: {resultado}", True, (255, 255, 0))
    texto_adicionar = fonte.render("ADICIONAR AO RANKING", True, (255, 255, 255))
    texto_voltar = fonte.render("VOLTAR", True, (255, 255, 255))

    # Retângulos dos botões
    area_botao_adicionar = pygame.Rect(100, 500, 250, 50)
    area_botao_voltar = pygame.Rect(450, 500, 200, 50)

    pontuacao_ja_salva = False  # evita trapaças
    while True: #                                   LAÇO DE EVENTOS

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: # registro de clique no botão esquedro

                # Clique no Botão Adicionar Pontuação
                if area_botao_adicionar.collidepoint(evento.pos) and not pontuacao_ja_salva:
                    # update(jogador, resultado)
                    ranking = carregar_top10()
                    pontuacao_ja_salva = True

                # Clique no Botão Voltar
                if area_botao_voltar.collidepoint(evento.pos):
                    return "game_over"
                
        #                                           ELEMENTOS NA TELA
        tela.fill((30, 30, 30))

        # Título e Resultado do Jogador
        tela.blit(texto_titulo, (270, 30))
        tela.blit(texto_resultado, (250, 440))

        # Lista do Top 10 Jogadores
        for i, jogador_ranking in enumerate(ranking):
            texto_jogador = fonte.render(
                f"{i + 1}º - {jogador_ranking['nome']} - {jogador_ranking['pontos']}",
                True,
                (255, 255, 255)
            )
            tela.blit(texto_jogador, (150, 80 + i * 35))

        # Botão Adicionar - Verde por padrão | Cinza se clicado
        cor_botao_adicionar = (100, 100, 100) if pontuacao_ja_salva else (0, 150, 0)
        pygame.draw.rect(tela, cor_botao_adicionar, area_botao_adicionar)
        tela.blit(texto_adicionar, (115, 512))

        # Botão Voltar
        pygame.draw.rect(tela, (150, 0, 0), area_botao_voltar)
        tela.blit(texto_voltar, (510, 512))

        pygame.display.flip()

        relogio.tick(60)  # pra dar 60 FPS