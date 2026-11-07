# 🎮 GameHub - Matchmaker & Balance Manager (v3.0)

## 📌 Análise do Produto
O GameHub é uma plataforma leve focada em vídeo-games que resolve o problema de jogadores que buscam parceiros ou querem montar equipes online para jogar seus títulos favoritos de forma equilibrada. Na versão 3.0, o sistema evoluiu de um pareamento simples para um **Matchmaking Inteligente Balanceado por Nível de Habilidade (Elo)**, além de incluir travas de capacidade máxima e gerenciamento do ciclo de vida das salas (status da partida).

---

## 📋 Especificação de Requisitos

### Requisitos Funcionais
*   **RF01 - Cadastro de Perfil e Rank:** O sistema deve permitir o cadastro de jogadores informando seus nicknames, jogos favoritos e seu nível de habilidade (Bronze, Prata, Ouro ou Platina).
*   **RF02 - Criação de Salas Parametrizadas:** O sistema deve permitir a criação de salas de busca de partida associadas a um jogo específico, um jogador host e uma capacidade máxima customizável de vagas.
*   **RF03 - Matchmaking Inteligente e Balanceado (NOVO - v3.0):** O sistema deve analisar de forma cruzada as preferências de jogos **E** o Elo dos usuários, adicionando-os automaticamente apenas às salas correspondentes e equilibradas.
*   **RF04 - Entrada e Gerenciamento Manual de Salas:** O sistema deve permitir que jogadores entrem manualmente em salas existentes utilizando o ID da sala, respeitando as validações de sala cheia ou partida já iniciada, além de permitir ao host forçar o início do jogo.
*   **RF05 - Listagem de Status do Servidor:** O sistema deve exibir a lista detalhada de jogadores ativos (com seus elos) e salas disponíveis (com participantes, vagas ocupadas e status atual) em tempo real na memória.

---

## 🏗️ Arquitetura e Estrutura
O projeto foi desenvolvido utilizando os conceitos de **Programação Orientada a Objetos (POO)**:

*   **Jogador:** Classe responsável por encapsular as informações do perfil do usuário e seu nível competitivo (Elo).
*   **Sala:** Classe responsável pelo gerenciamento de vagas, participantes, regras de entrada e ciclo de vida/estado do lobby de jogo.

---

## 🚀 Como Executar o Programa

1. Certifique-se de ter o Python 3.x instalado em sua máquina.
2. Clone ou baixe este repositório.
3. Execute o arquivo principal pelo terminal com o comando:
   ```bash
   python app.py
   ```
