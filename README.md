# gamehub-projeto

# 🎮 GameHub - Matchmaker & Library Manager

Este projeto foi desenvolvido para a **Atividade Contínua 01** da disciplina de *Software Product: Analysis, Specification, Project & Implementation* do professor Antonio de Oliveira Dias.

## 📌 Análise do Produto
O GameHub é uma plataforma focada em vídeo-games que resolve o problema de jogadores que jogam sozinhos e têm dificuldade para encontrar parceiros ou montar equipes online com os mesmos interesses. O sistema foi expandido para integrar um módulo de IA e busca que fornece dados completos sobre títulos clássicos e lançamentos do mercado.

## 📋 Especificação de Requisitos

### Requisitos Funcionais (RF)
- **RF01 - Cadastro de Jogador:** O sistema deve permitir o cadastro de jogadores e a seleção de seus jogos favoritos.
- **RF02 - Criação de Salas:** O sistema deve permitir a criação de salas de matchmaking por jogo para reunir equipes.
- **RF03 - Consulta de Jogos (IA Local):** O sistema deve fornecer ficha técnica detalhada (sinopse, classificação, empresa) para jogos específicos como GTA V, GTA IV, GTA San Andreas, GTA Vice City, Red Dead Redemption 2, Skyrim, Cyberpunk 2077 e Far Cry 3.
- **RF04 - Busca Infinita (API Global):** Caso o usuário busque um jogo fora do catálogo local, o sistema deve realizar uma chamada de API externa em tempo real para obter os dados de identificação e o melhor preço de mercado.

### Requisitos Não-Funcionais (RNF)
- **RNF01 - Integração de Dados:** O sistema deve consumir dados de uma API pública externa (CheapShark API) para buscas globais.
- **RNF02 - Usabilidade:** O sistema deve rodar de maneira leve e direta por meio de um menu interativo no terminal.

## 🚀 Como Abrir e Executar o Programa
Para rodar este projeto na sua máquina, siga os passos abaixo:

1. Certifique-se de ter o **Python** instalado no seu computador.
2. Abra o terminal na pasta onde o arquivo `app.py` está salvo.
3. Digite o seguinte comando e aperte Enter:
   ```bash
   python app.py
   ```
