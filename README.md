# gamehub-projeto

# 🎮 GameHub - Matchmaker & Library Manager

## 📌 Análise do Produto
O GameHub é uma plataforma focada em vídeo-games que resolve o problema de jogadores que jogam sozinhos e têm dificuldade para encontrar parceiros ou montar equipes online. O sistema conta com um módulo de IA Histórica conectado a bases de dados globais para analisar e descrever jogos desde a geração **PlayStation 1 (PS1) até o PlayStation 5 (PS5)**.

## 📋 Especificação de Requisitos

### Requisitos Funcionais (RF)
- **RF01 - Cadastro de Jogador:** O sistema deve permitir o cadastro de jogadores e a seleção de seus jogos favoritos.
- **RF02 - Criação de Salas:** O sistema deve permitir a criação de salas de matchmaking por jogo para reunir equipes.
- **RF03 - Consulta de Jogos via IA Histórica (Todos os Consoles):** O sistema deve buscar dados dinamicamente de qualquer jogo da história (gerações PlayStation, Nintendo, Sega, Xbox, PC, etc.) exibindo títulos oficiais e sinopses em tempo real.

### Requisitos Não-Funcionais (RNF)
- **RNF01 - Integração com API Externa:** O sistema deve consumir dados de uma API pública em tempo real para obter informações de jogos sem depender de armazenamento local rígido.
- **RNF02 - Robustez na Busca:** O sistema deve tratar strings e buscas de forma flexível para aceitar variações de nomes digitados pelos usuários.

## 🚀 Como Abrir e Executar o Programa
Para rodar este projeto na sua máquina, siga os passos abaixo:

1. Certifique-se de ter o **Python** instalado no seu computador.
2. Abra o terminal na pasta onde o arquivo `app.py` está salvo.
3. Digite o seguinte comando e aperte Enter:
   ```bash
   python app.py
   ```
