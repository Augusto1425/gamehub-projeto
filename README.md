# 🎮 GameHub - Matchmaker & Library Manager (v2.0)

## 📌 Análise do Produto
O **GameHub** é uma plataforma leve focada em vídeo-games que resolve o problema de jogadores que buscam parceiros ou querem montar equipes online para jogar seus títulos favoritos. Na versão 2.0, o sistema evoluiu para incluir **algoritmos automáticos de pareamento** e gestão de participantes dentro de salas ativas.

---

## 📋 Especificação de Requisitos

### Requisitos Funcionais
* **RF01 - Cadastro de Perfil:** O sistema deve permitir o cadastro de jogadores informando seus nicknames e jogos favoritos.
* **RF02 - Criação de Salas:** O sistema deve permitir a criação de salas de busca de partida associadas a um jogo específico e a um jogador *host*.
* **RF03 - Matchmaking Automático (NOVO - AC02):** O sistema deve analisar as preferências de jogos dos usuários e adicioná-los automaticamente às salas correspondentes.
* **RF04 - Entrada Manual em Salas (NOVO - AC02):** O sistema deve permitir que jogadores cadastrados entrem manualmente em salas existentes utilizando o ID da sala.
* **RF05 - Listagem de Status:** O sistema deve exibir a lista detalhada de jogadores ativos e salas disponíveis (com participantes) em tempo real na memória.

---

## 🏗️ Arquitetura e Estrutura
O projeto foi refatorado utilizando os conceitos de **Programação Orientada a Objetos (POO)**:
* `Jogador`: Classe responsável por encapsular as informações do perfil do usuário.
* `Sala`: Classe responsável pelo gerenciamento dos participantes e regras da sala de jogo.

---

## 🚀 Como Executar o Programa
1. Certifique-se de ter o Python 3.x instalado em sua máquina.
2. Clone ou baixe este repositório.
3. Execute o arquivo principal pelo terminal com o comando:
   ```bash
   python main.py
   
