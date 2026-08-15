import os
import pygame

pygame.font.init()

PAINEL_AZUL = (30, 45, 70)
AMARELO = (255, 205, 90)
VERMELHO_PONTOS = (220, 40, 40)
LARANJA_TITULO = (255, 140, 40)

FONTE_VALOR = pygame.font.SysFont("couriernew", 30, bold=True)


def _caminho_fundo():
    pasta = os.path.dirname(os.path.abspath(__file__))
    for sub in ("Imagens", os.path.join("..", "Imagens"), "assets", ""):
        caminho = os.path.join(pasta, sub, "game_over_fundo.png")
        if os.path.isfile(caminho):
            return caminho
    raise FileNotFoundError(f"game_over_fundo.png não encontrado perto de {pasta}")


CAMINHO_FUNDO = _caminho_fundo()


def formatar_tempo(s):
    return f"{int(s // 3600):02d}:{int(s % 3600 // 60):02d}:{int(s % 60):02d}"


def tela_game_over(tela, pontuacao, melhor_pontuacao, tempo_total):
    """Retorna 'jogar_novamente' | 'ranking' | 'sair'."""
    largura, altura = tela.get_size()
    fundo = pygame.transform.smoothscale(pygame.image.load(CAMINHO_FUNDO).convert(), (largura, altura))
    ex, ey = largura / 555, altura / 1024

    def rel(x, y, w, h):
        return pygame.Rect(int(x * ex), int(y * ey), int(w * ex), int(h * ey))

    area_tempo = rel(370, 186, 180, 45)
    area_pontuacao = rel(370, 288, 180, 45)
    botoes = {
        "jogar_novamente": rel(120, 815, 315, 45),
        "ranking": rel(120, 863, 315, 42),
        "sair": rel(120, 908, 315, 42),
    }

    clock = pygame.time.Clock()
    while True:
        clique = None
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                return "sair"
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                clique = evento.pos

        mouse = pygame.mouse.get_pos()
        tela.blit(fundo, (0, 0))

        for area, valor, cor in (
            (area_tempo, formatar_tempo(tempo_total), AMARELO),
            (area_pontuacao, pontuacao, VERMELHO_PONTOS if pontuacao == 0 else AMARELO),
        ):
            pygame.draw.rect(tela, PAINEL_AZUL, area)
            texto = FONTE_VALOR.render(str(valor), True, cor)
            tela.blit(texto, texto.get_rect(midright=area.midright))

        for acao, area in botoes.items():
            if area.collidepoint(mouse):
                pygame.draw.rect(tela, LARANJA_TITULO, area, width=2, border_radius=6)
            if clique and area.collidepoint(clique):
                return acao

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    tela = pygame.display.set_mode((555, 1024))
    pygame.display.set_caption("Game Over")
    print(tela_game_over(tela, pontuacao=0, melhor_pontuacao=1540, tempo_total=5025))
    pygame.quit()