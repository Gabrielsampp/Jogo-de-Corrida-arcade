import random
from pathlib import Path

# 1. Descobre o caminho da pasta raiz do projeto (subindo 2 níveis a partir deste arquivo)
# __file__ -> Jogo/get_images.py
# .parent -> pasta Jogo
# .parent.parent -> raiz do projeto (onde está a pasta "Imagens")
BASE_DIR = Path(__file__).resolve().parent.parent
IMAGENS_DIR = BASE_DIR / "Imagens"


pistas = {
    "deserto" : "pista_deserto", 
    "asfalto" : "pista_cidade", 
    "antártida" : "pista_gelo", 
    "Campos verdes" : "pista_campos_verdes", 
}
def get_bg_pista(pista: str) -> list[Path]:
    """Retorna uma lista com o caminho de duas imagens para a pista selecionada."""
    # Exemplo: Procura imagens como "pista_asfalto_1.png", "pista_asfalto_2.png"
    # ou arquivos organizados em subpastas dentro de Imagens.
    
    caminho_pista1 = IMAGENS_DIR / f"{pistas[pista]}_1.png"
    caminho_pista2 = IMAGENS_DIR / f"{pistas[pista]}_2.png"

    return [caminho_pista1, caminho_pista2]


def get_carro(carro: str) -> Path:
    """Retorna o caminho da imagem do carro selecionado."""
    caminho_carro = IMAGENS_DIR / f"carro_{carro}.png"

    return caminho_carro


def get_obstaculos(qtd: int) -> list[Path]:
    """Retorna uma lista de caminhos de imagens de obstáculos de tamanho qtd.
    
    Mapeia todos os obstáculos disponíveis na pasta e sorteia 'qtd' deles.
    """
    pasta_obstaculos = IMAGENS_DIR / "obstaculos"

    # .glob() busca todos os arquivos da extensão indicada dentro da pasta
    todas_imagens = list(IMAGENS_DIR.glob("carro*"))

    if not todas_imagens:
        raise FileNotFoundError(f"Nenhuma imagem encontrada em {pasta_obstaculos}")

    # Sorteia 'qtd' imagens da lista de disponíveis (pode repetir se qtd > tamanho)
    obstaculos_escolhidos = random.choices(todas_imagens, k=qtd)

    return obstaculos_escolhidos