import pygame
import sys
import os
from dataclasses import dataclass

# Tela de criação de pista como função
# Para usar: importar tela_pista() e chamar. Retorna uma instância de Pista ou None se cancelado.

LARGURA = 500
ALTURA = 700

# Ajuste do diretório de imagens: procura pela pasta 'Imagens' um nível acima de 'telas'.
def caminho_imagem(*parts):
    base = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'Imagens'))
    return os.path.join(base, *parts)


@dataclass
class Pista:
    nome: str
    quantidade_obstaculos: int
    velocidade: int
    id_pista: str
    pista: str
    carro: str
    publica: bool


class Botao:
    def __init__(self, x, y, largura, altura, texto=""):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.selecionado = False

    def desenhar(self, tela, fonte):
        cor = (40, 150, 255) if self.selecionado else (70, 75, 85)
        pygame.draw.rect(tela, cor, self.rect, border_radius=8)
        pygame.draw.rect(tela, (200, 200, 200), self.rect, 2, border_radius=8)
        imagem = fonte.render(self.texto, True, (255, 255, 255))
        tela.blit(imagem, imagem.get_rect(center=self.rect.center))

    def clicou(self, posicao):
        return self.rect.collidepoint(posicao)


class BotaoImagem:
    def __init__(self, x, y, largura, altura, imagem_surface, label=""):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.imagem = imagem_surface
        self.selecionado = False
        self.label = label

    def desenhar(self, tela, fonte_label=None):
        cor = (40, 150, 255) if self.selecionado else (60, 65, 75)
        pygame.draw.rect(tela, cor, self.rect, border_radius=8)
        pygame.draw.rect(tela, (220, 220, 220), self.rect, 2, border_radius=8)
        if self.imagem:
            img_rect = self.imagem.get_rect(center=self.rect.center)
            tela.blit(self.imagem, img_rect)
        if fonte_label and self.label:
            etiqueta = fonte_label.render(self.label, True, (230, 230, 230))
            pos = (self.rect.centerx, self.rect.bottom + 12)
            tela.blit(etiqueta, etiqueta.get_rect(center=pos))

    def clicou(self, posicao):
        return self.rect.collidepoint(posicao)


class CampoTexto:
    def __init__(self, x, y, largura, altura, fonte, texto_inicial=""):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto_inicial
        self.ativo = False
        self.fonte = fonte

    def desenhar(self, tela):
        cor_fundo = (50, 55, 60) if not self.ativo else (70, 80, 95)
        pygame.draw.rect(tela, cor_fundo, self.rect, border_radius=6)
        pygame.draw.rect(tela, (200, 200, 200), self.rect, 2, border_radius=6)
        imagem = self.fonte.render(self.texto, True, (255, 255, 255))
        tela.blit(imagem, (self.rect.x + 6, self.rect.y + (self.rect.height - imagem.get_height()) // 2))

    def clicou(self, pos):
        return self.rect.collidepoint(pos)

    def tratar_evento(self, evento):
        if evento.type == pygame.KEYDOWN and self.ativo:
            if evento.key == pygame.K_BACKSPACE:
                self.texto = self.texto[:-1]
            elif evento.key == pygame.K_RETURN:
                self.ativo = False
            else:
                # Limitar comprimento para evitar overflow visual
                if len(self.texto) < 30:
                    self.texto += evento.unicode


def carregar_imagem(path, tamanho=None, flip=False):
    try:
        surf = pygame.image.load(path).convert_alpha()
        if tamanho:
            surf = pygame.transform.smoothscale(surf, tamanho)
        if flip:
            surf = pygame.transform.flip(surf, True, False)
        return surf
    except Exception:
        # placeholder
        w, h = tamanho if tamanho else (60, 60)
        s = pygame.Surface((w, h), pygame.SRCALPHA)
        s.fill((120, 120, 120))
        pygame.draw.rect(s, (200, 200, 200), s.get_rect(), 2)
        return s


def tela_pista():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Criar Pista")
    fonte = pygame.font.Font(None, 22)
    fonte_titulo = pygame.font.Font(None, 28)
    fonte_label = pygame.font.Font(None, 18)
    clock = pygame.time.Clock()

    # Campos de texto
    campo_nome = CampoTexto(20, 70, 340, 36, fonte)
    campo_obst = CampoTexto(20, 120, 120, 36, fonte)
    campo_vel = CampoTexto(160, 120, 120, 36, fonte)
    campo_id = CampoTexto(20, 170, 260, 36, fonte)

    # Botões de visibilidade
    botao_publico = Botao(80, 510, 150, 55, "PÚBLICA")
    botao_privado = Botao(270, 510, 150, 55, "PRIVADA")
    botao_publico.selecionado = True
    pista_publica = True

    # Botão criar
    botao_criar = Botao(150, 610, 200, 60, "CRIAR PISTA")

    # Pistas (substitui o antigo 'relevos')
    pistas = [
        ("cidade_1", caminho_imagem('cidade_1.png')),
        ("cidade_2", caminho_imagem('cidade_2.png')),
        ("campos_verdes_1", caminho_imagem('campos_verdes_1.png')),
        ("campos_verdes_2", caminho_imagem('campos_verdes_2.png')),
    ]

    botoes_pista = []
    # Layout calculado para evitar sobreposição
    margem = 20
    largura_botao_pista = 100
    espacamento_pista = 12
    Np = len(pistas)
    total_pista = Np * largura_botao_pista + (Np - 1) * espacamento_pista
    start_x_pista = (LARGURA - total_pista) // 2
    y_pista = 220
    for i, (nome_pista, path) in enumerate(pistas):
        x = start_x_pista + i * (largura_botao_pista + espacamento_pista)
        img = carregar_imagem(path, (90, 70))
        bot = BotaoImagem(x, y_pista, largura_botao_pista, 90, img, label=nome_pista.replace('_',' ').capitalize())
        botoes_pista.append((bot, nome_pista))

    pista_selecionada = None

    # Carros (usar imagens fornecidas)
    lista_carros = [
        ('carro_azul', caminho_imagem('carro_azul.png')),
        ('carro_verde', caminho_imagem('carro_verde.png')),
        ('carro_roxo', caminho_imagem('carro_roxo.png')),
        ('carro_amarelo', caminho_imagem('carro_amarelo.png')),
        ('carro_vermelho', caminho_imagem('carro_vermelho.png')),
    ]

    botoes_carro = []
    largura_botao_carro = 85
    espacamento_carro = 12
    Nc = len(lista_carros)
    total_carro = Nc * largura_botao_carro + (Nc - 1) * espacamento_carro
    start_x_carro = (LARGURA - total_carro) // 2
    y_carro = 390
    for i, (nome_carro, path) in enumerate(lista_carros):
        img = carregar_imagem(path, (60, 80))
        x = start_x_carro + i * (largura_botao_carro + espacamento_carro)
        bot = BotaoImagem(x, y_carro, largura_botao_carro, 100, img, label="")
        botoes_carro.append((bot, nome_carro))

    carro_selecionado = None

    mensagem_erro = ""
    tempo_erro = 0

    rodando = True
    pista_criada = None

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                pos = evento.pos
                # Campos
                if campo_nome.clicou(pos):
                    campo_nome.ativo = True
                    campo_obst.ativo = False
                    campo_vel.ativo = False
                    campo_id.ativo = False
                elif campo_obst.clicou(pos):
                    campo_nome.ativo = False
                    campo_obst.ativo = True
                    campo_vel.ativo = False
                    campo_id.ativo = False
                elif campo_vel.clicou(pos):
                    campo_nome.ativo = False
                    campo_obst.ativo = False
                    campo_vel.ativo = True
                    campo_id.ativo = False
                elif campo_id.clicou(pos):
                    campo_nome.ativo = False
                    campo_obst.ativo = False
                    campo_vel.ativo = False
                    campo_id.ativo = True
                else:
                    # clicar fora desativa
                    campo_nome.ativo = campo_obst.ativo = campo_vel.ativo = campo_id.ativo = False

                # Pistas
                for i, (bot, nome_pista) in enumerate(botoes_pista):
                    if bot.clicou(pos):
                        pista_selecionada = nome_pista
                        for b, _ in botoes_pista:
                            b.selecionado = False
                        bot.selecionado = True

                # Carros
                for i, (bot, nome_carro) in enumerate(botoes_carro):
                    if bot.clicou(pos):
                        carro_selecionado = nome_carro
                        for b, _ in botoes_carro:
                            b.selecionado = False
                        bot.selecionado = True

                # Visibilidade
                if botao_publico.clicou(pos):
                    pista_publica = True
                    botao_publico.selecionado = True
                    botao_privado.selecionado = False
                if botao_privado.clicou(pos):
                    pista_publica = False
                    botao_publico.selecionado = False
                    botao_privado.selecionado = True

                # Criar
                if botao_criar.clicou(pos):
                    # validações básicas
                    nome = campo_nome.texto.strip()
                    obst = campo_obst.texto.strip()
                    vel = campo_vel.texto.strip()
                    idp = campo_id.texto.strip()

                    if not nome:
                        mensagem_erro = "Preencha o nome da pista"
                    elif not obst.isdigit():
                        mensagem_erro = "Obstáculos deve ser um número"
                    elif not vel.isdigit():
                        mensagem_erro = "Velocidade deve ser um número"
                    elif pista_selecionada is None:
                        mensagem_erro = "Selecione a pista"
                    elif carro_selecionado is None:
                        mensagem_erro = "Selecione um carro"
                    else:
                        pista_criada = Pista(
                            nome=nome,
                            quantidade_obstaculos=int(obst),
                            velocidade=int(vel),
                            id_pista=idp or nome,
                            pista=pista_selecionada,
                            carro=carro_selecionado,
                            publica=pista_publica,
                        )
                        print("Pista criada:")
                        print(pista_criada)
                        rodando = False
                        break
                    tempo_erro = pygame.time.get_ticks()

            elif evento.type == pygame.KEYDOWN:
                campo_nome.tratar_evento(evento)
                campo_obst.tratar_evento(evento)
                campo_vel.tratar_evento(evento)
                campo_id.tratar_evento(evento)

        # Desenho
        tela.fill((35, 40, 45))
        # Título (centralizado)
        titulo_surf = fonte_titulo.render("CRIAR NOVA PISTA", True, (255, 255, 255))
        tela.blit(titulo_surf, titulo_surf.get_rect(center=(LARGURA//2, 28)))

        # Labels dos campos
        tela.blit(fonte_label.render("Nome:", True, (230, 230, 230)), (20, 50))
        tela.blit(fonte_label.render("Obstáculos:", True, (230, 230, 230)), (20, 100))
        tela.blit(fonte_label.render("Velocidade:", True, (230, 230, 230)), (160, 100))
        tela.blit(fonte_label.render("ID:", True, (230, 230, 230)), (20, 150))

        # Campos
        campo_nome.desenhar(tela)
        campo_obst.desenhar(tela)
        campo_vel.desenhar(tela)
        campo_id.desenhar(tela)

        # Seção pista
        tela.blit(fonte_titulo.render("PISTA", True, (255, 255, 255)), fonte_titulo.render("PISTA", True, (255,255,255)).get_rect(center=(LARGURA//2, 200)))
        for bot, _ in botoes_pista:
            bot.desenhar(tela, fonte_label)

        # Seção carro
        tela.blit(fonte_titulo.render("CARRO DO PLAYER", True, (255, 255, 255)), fonte_titulo.render("CARRO DO PLAYER", True, (255,255,255)).get_rect(center=(LARGURA//2, 340)))
        for bot, _ in botoes_carro:
            bot.desenhar(tela, fonte_label)

        # Visibilidade
        tela.blit(fonte_titulo.render("VISIBILIDADE DA PISTA", True, (255, 255, 255)), fonte_titulo.render("VISIBILIDADE DA PISTA", True, (255,255,255)).get_rect(center=(LARGURA//2, 470)))
        botao_publico.desenhar(tela, fonte)
        botao_privado.desenhar(tela, fonte)

        # Criar botão
        botao_criar.desenhar(tela, fonte)

        # Mensagem de erro temporária
        if mensagem_erro:
            if pygame.time.get_ticks() - tempo_erro < 3000:
                err = fonte.render(mensagem_erro, True, (255, 100, 100))
                tela.blit(err, (20, 580))
            else:
                mensagem_erro = ""

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    # Retorna o objeto Pista criado ou None
    return pista_criada


if __name__ == '__main__':
    # Permite testar o módulo isoladamente
    pista = tela_pista()
    if pista:
        print('Objeto Pista retornado:', pista)
    else:
        print('Nenhuma pista criada.')
    sys.exit()
