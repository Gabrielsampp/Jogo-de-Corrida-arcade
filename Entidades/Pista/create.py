#FUNÇÃO CREATE - PISTA

import json
from pathlib import Path
from get_last_id import get_last_id

tipos_de_relevo = ["deserto", "asfalto", "antártida", "campos verdes"] 

#                                                   FUNÇÃO PRINCIPAL
def cadastrar_pista(
    nome: str,
    is_public: bool,
    tipo_relevo: str,
    velocidade: float,
    qtd_obstaculos: int,
    cor: str,
    caminho_arquivo: str = "Entidades/Pista/pista.json"
):
    # Relevo                                      Validações de entradas
    if tipo_relevo.lower() not in tipos_de_relevo:
        return (False, f"Tipo de relevo inválido. Permitidos: {tipos_de_relevo}")
    # Velocidade
    try:
        velocidade_num = float(velocidade)
        if velocidade_num <= 0:
            return (False, "A velocidade deve ser maior que zero.")
    except (ValueError, TypeError):
        return (False, "A velocidade precisa ser um número válido (ex: 15.0).")

    # Obstáculos
    try:
        qtd_obstaculos_num = int(qtd_obstaculos)
        if qtd_obstaculos_num < 0:
            return (False, "A quantidade de obstáculos não pode ser negativa.")
    except (ValueError, TypeError):
        return (False, "A quantidade de obstáculos precisa ser um número inteiro (ex: 5).")

    try: #                                                  Manipulação no arquivo

        ultimo = get_last_id() # Elaboração de um novo ID
        novo_id = (ultimo if ultimo is not None else 0) + 1

        nova_pista = { #                                    Novos dados da pista.
            "id": novo_id,
            "nome": nome,
            "is_public": is_public,
            "tipo_de_relevo": tipo_relevo,
            "velocidade": float(velocidade),
            "quantidade_obstaculos": int(qtd_obstaculos),
            "melhor_desempenho": 0,
            "jogador_de_melhor_desempenho": "",
            "carro": str(cor)
        }
        
        dados = {"pistas": []}
        caminho = Path(caminho_arquivo)

        # Leitura
        if caminho.exists():
            with caminho.open("r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read().strip()

                if conteudo:
                    dados = json.loads(conteudo)

                    if "pistas" not in dados:
                        dados["pistas"] = []

        dados["pistas"].append(nova_pista)

        # Escrita
        caminho.parent.mkdir(parents=True, exist_ok=True)
        with caminho.open("w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

        return (True, f"Pista '{nome}' cadastrada com sucesso com o ID {novo_id}.")

    except Exception as erro:
        return (False, f"Falha ao cadastrar a pista: {str(erro)}")