#FUNÇÃO CREATE - PISTA

import json
import os
from get_last_id import get_last_id  # Importa a função existente de get_last_id.py

tipos_de_relevo = ["deserto", "asfalto", "antártida", "Campos verdes"] #uso básico de uma lista

# Função para criar as pistas.

def cadastrar_pista(
    nome: str,
    is_public: bool,
    tipo_relevo: list[str],
    velocidade: float,
    qtd_obstaculos: int,
    caminho_arquivo: str = "Entidades/Pista/pista.json",
):
    # Validação dos tipos de relevo

    if isinstance(tipo_relevo, str):
        if tipo_relevo not in tipos_de_relevo:
            return (False, f"Tipo de relevo inválido. Permitidos: {tipos_de_relevo}")
        
    elif isinstance(tipo_relevo, list):
        if not tipo_relevo or not all(r in tipos_de_relevo for r in tipo_relevo):
            return (False, f"Tipo de relevo inválido. Permitidos: {tipos_de_relevo}")
        
    else:
        return (False, "Formato do tipo de relevo é inválido.")

    # Gera um novo ID, usando a função importada do arquivo get_last_id.py.

    ultimo = get_last_id()
    novo_id = (ultimo if ultimo is not None else 0) + 1

    # Gera um dicionário com os novos dados da pista.
    nova_pista = {
        "id": novo_id,
        "nome": nome,
        "is_public": bool(is_public),
        "tipo_de_relevo": tipo_relevo,
        "velocidade": float(velocidade),
        "quantidade_obstaculos": int(qtd_obstaculos),
        "melhor_desempenho": "",
        "jogador_de_melhor_desempenho": ""
    }

    # Leitura e verificaçao dos novos dados no arquivo
    try:
        dados = {"pistas": []}

        if os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read().strip()

                if conteudo:
                    dados = json.loads(conteudo)

                    if "pistas" not in dados:
                        dados["pistas"] = []

        dados["pistas"].append(nova_pista)

    # Escrita dos novos dados no arquivo
    
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

        return (True, f"Pista '{nome}' cadastrada com sucesso com o ID {novo_id}.")

    except Exception as erro:
        return (False, f"Falha ao salvar no arquivo JSON: {str(erro)}")