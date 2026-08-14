#FUNÇÃO CREATE - PISTA

import json
from pathlib import Path
from get_last_id import get_last_id

tipos_de_relevo = ["deserto", "asfalto", "antártida", "Campos verdes"] 

def cadastrar_pista( #                                       FUNÇÃO PRINCIPAL
    nome: str,
    is_public: bool,
    tipo_relevo: list[str],
    velocidade: float,
    qtd_obstaculos: int,
    cor: str,
    caminho_arquivo: str = "Entidades/Pista/pista.json"
):
    if isinstance(tipo_relevo, str): #                      Validação dos tipos de relevo                 
        if tipo_relevo not in tipos_de_relevo:
            return (False, f"Tipo de relevo inválido. Permitidos: {tipos_de_relevo}")
        
    elif isinstance(tipo_relevo, list):
        if not tipo_relevo or not all(r in tipos_de_relevo for r in tipo_relevo):
            return (False, f"Tipo de relevo inválido. Permitidos: {tipos_de_relevo}")
        
    else:
        return (False, "Formato do tipo de relevo é inválido.")

    ultimo = get_last_id() #                                Elaboração de um novo ID
    novo_id = (ultimo if ultimo is not None else 0) + 1

    nova_pista = { #                                        Novos dados da pista.
        "id": novo_id,
        "nome": nome,
        "is_public": bool(is_public),
        "tipo_de_relevo": tipo_relevo,
        "velocidade": float(velocidade),
        "quantidade_obstaculos": int(qtd_qtd_obstaculos if 'qtd_qtd_obstaculos' in locals() else qtd_obstaculos),
        "melhor_desempenho": "",
        "jogador_de_melhor_desempenho": "",
        "carro": str(cor)
    }

    try: #                                                  Manipulação no arquivo
        dados = {"pistas": []}
        caminho = Path(caminho_arquivo)

        # Leitura
        if caminho.exists():
            conteudo = caminho.read_text(encoding="utf-8").strip()

            if conteudo:
                dados = json.loads(conteudo)

                if "pistas" not in dados:
                    dados["pistas"] = []

        dados["pistas"].append(nova_pista)

        # Escrita
        caminho.parent.mkdir(parents=True, exist_ok=True)
        caminho.write_text(json.dumps(dados, ensure_ascii=False, indent=4), encoding="utf-8")

        return (True, f"Pista '{nome}' cadastrada com sucesso com o ID {novo_id}.")

    except Exception as erro:
        return (False, f"Falha ao salvar no arquivo JSON: {str(erro)}")