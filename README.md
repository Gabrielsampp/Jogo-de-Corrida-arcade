# 🏎️ Jogo de Corrida Arcade

> **Projeto Final - Introdução à Programação (2026.1)**  
> Um jogo de corrida estilo arcade com geração infinita de pistas, criação customizada de cenários, ranking global e sistema completo de gerenciamento via terminal.

---

## 📌 Sumário
- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades Principais](#-funcionalidades-principais)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Modelagem de Dados (Entidades)](#-modelagem-de-dados-entidades)
- [Equipe de Desenvolvimento](#-equipe-de-desenvolvimento)
- [Como Executar](#-como-executar)

---

## 🎯 Sobre o Projeto

### O Problema
Criar uma comunidade em torno de um jogo de corrida arcade simples e divertido, permitindo que jogadores compitam em rankings gerais, personalizem e compartilhem suas próprias pistas, mantendo o ambiente organizado através de uma curadoria/gerenciamento administrativo restrito.

### O Jogo
Desenvolvido com a biblioteca **Pygame**, o jogo desafia o jogador a pilotar e desviar de obstáculos e outros veículos na pista pelo maior tempo possível. 
* **Pistas Infinitas:** Disposição aleatória de obstáculos.
* **Bônus:** Power-ups e itens bônus surgem aleatoriamente ao longo da corrida.
* **Estilo Visual:** Design retrô em *Pixel Art*.

### Armazenamento e Persistência
Todos os dados de usuários, pistas e rankings são mantidos através de **armazenamento estático em arquivos JSON**.

---

## 🚀 Funcionalidades Principais

### 🎮 Interface do Jogo (Pygame)
* **Tela Inicial:** Opção direta para dar `PLAY` no jogo.
* **Tela de Corrida (Game Loop):**
  * Controle do veículo do jogador.
  * Lógica de pistas infinitas.
  * Geração dinâmica de obstáculos e bônus.
  * Detecção de colisão e cálculo/acúmulo de pontuação.
* **Tela de Game Over:** Opção para recomeçar a partida ou acessar a tabela de ranking.
* **Tela de Ranking:** Exibição dos melhores desempenhos salvos no arquivo `ranking.json`.
* **Tela de Criação de Pistas:**
  * Escolha de relevo (*Deserto*, *Asfalto*, *Antártida*, *Campos Verdes*).
  * Configuração da quantidade de obstáculos e velocidade da pista.
  * Seleção do carro do jogador.

### 💻 Sistema no Terminal / CMD
* **Menu Inicial:**
  * Login de Jogador e Login de Admin.
  * Cadastro de novo jogador.
  * Consulta do ranking geral.
  * Validação e tratamento de dados (`try/except`).
* **Painel Administrativo:**
  * Métricas em cabeçalho (total de entidades cadastradas).
  * Buscar e remover jogadores ou pistas especificadas.
  * Atualizar dados cadastrais do admin.
* **Painel do Jogador:**
  * Iniciar jogo escolhendo a pista desejada.
  * Criar e personalizar pistas públicas ou privadas.
  * Explorar pistas da comunidade e verificar histórico/resultados.
  * Alteração de senha e dados cadastrais.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.12.1
* **Interface Gráfica do Jogo:** Biblioteca Pygame (https://pypi.org/project/pygame/)
<!-- * **Customização do terminal:** Biblioteca Rich (https://pypi.org/project/rich/) -->
* **Persistência de Dados:** Arquivos JSON

---

## 🏗️ Estrutura do Projeto

O projeto adota uma arquitetura modularizada para facilitar a colaboração via Git:

```text
📂 Jogo-de-Corrida-arcade
 ├── 📂 Entidades
 │    ├── 📂 Jogador
 │    │    ├── jogador.py
 │    │    ├── create.py
 │    │    ├── get_by_user_name.py
 │    │    ├── get_all.py
 │    │    ├── update.py
 │    │    ├── delete.py
 │    │    ├── validation.py
 │    │    └── jogador.json
 │    ├── 📂 Pista
 │    │    ├── pista.py
 │    │    ├── create.py
 │    │    ├── get_all.py
 │    │    ├── get_by_list_id.py
 │    │    ├── get_publics.py
 │    │    ├── update.py
 │    │    ├── delete.py
 │    │    └── pista.json
 │    ├── 📂 Admin
 │    │    ├── admin.py
 │    │    ├── get.py
 │    │    ├── update.py
 │    │    ├── validation.py
 │    │    └── admin.json
 │    └── 📂 Ranking
 │         ├── ranking.py
 │         ├── add_player.py
 │         ├── remove_player.py
 │         ├── get_all.py
 │         ├── update.py
 │         ├── delete.py
 │         └── ranking.json
 ├── 📂 Imagens
 ├── 📂 Musicas
 ├── 📂 Jogo
 |    ├── jogo.py
 |    ├── get_images.py
 |    ├── tela_game_over.py
 |    ├── tela_inicial.py
 |    ├── tela_pista.py
 |    ├── tela_principal.py
 |    ├── tela_ranking.py
 ├── 📂 Sistema
 |    ├── menu_inicial.py
 |    ├── sistema_admin.py
 |    ├── sistema_jogador.py
 |    ├── sistema.py
 ├── main.py  
 ├── testes_entidades.py  
```

---


## Modelagem de Dados (Entidades)

* ### **Admin:** Terá controle sobre as entidades cadastradas, podendo excluí-los.

* ### **Jogador:** quem poderá jogar de fato

* ### **Pista:** customização de jogo.

* ### **Ranking:** lista de todos os melhores desempenhos dos jogadores;

---

## Equipe de Desenvolvimento e atribuições

```

Antônio Gabriel Sampaio | @Gabrielsampp
 - Arquitetura do projeto
 - Admin / admin
 - Pista / get_by_list_id
 - Jogador / create
 - Ranking / update
 - Jogo / tela_inicial
 - Sistema / sistema

Caio de Oliveira Ferreira Sá | @CaioOliveira-456
 - Ranking / add_player
 - Admin / login
 - Pista / get_all
 - Jogador / get_by_username
 - Ranking / remove_player
 - Sistema / menu_inicial
 - Refatoração (inglês)

Davi Henrique de Oliveira Maia  |  @davibr123
 - Admin / update
 - Jogador  / login
 - Pista / delete
 - jogo / tela_game_over
 - Sistema / sistema_admin
 - Imagens

José Alisson Dias Costa  |  @Alisson014
 - Jogador / delete
 - Pista / update
 - Pista / get_last_id
 - Jogo / tela_principal
 - Jogo / get_images
 - Revisões de código
 - Testes

Wanderson Francisco Lobo Almeida  |  @wandersonlobo
 - Jogador / get_all
 - Admin / get
 - Pista / get_publics
 - Ranking / delete
 - Ranking / get_all
 - Jogo / tela_pista
 - main.py

Wellington Dantas Angelo  |  @Angel0ps
Pista / create
 - Jogo / tela_ranking
 - Pista / pista
 - Jogador / update
 - Sistema / sistema_jogador
 - README.md

```

---

## 💻 Como Executar

### Clone o repositório em sua máquina
```bash
# Via SSH
git clone git@github.com:Gabrielsampp/Jogo-de-Corrida-arcade.git

# Via HTTPS
git clone https://github.com/Gabrielsampp/Jogo-de-Corrida-arcade.git
```

### Dependências

Certifique-se de utilizar uma versão do python entre a 3.8 e a 3.12.10. 

No momento em que este projeto foi desenvolvido, a biblioteca pygame apresentava incompatibilidade com versões do python superiores a 3.12.10.

```bash
# Para verificar a versão instalada do python:
python --version

# Instalar biblioteca pygame:
pip install pygame

# Demais bibliotecas utilizadas, como json, pathlib, datetime e random, são integradas nativamente na instalação padrão do python.
```

### Execução:
```bash
# Certifique-se de estar na pasta raiz do projeto.

python main.py

```


