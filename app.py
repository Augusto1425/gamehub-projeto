# =======================================================
# PROJETO GAMEHUB - ENGENHARIA DE PRODUTO & IA DE GAMES
# BUSCA GLOBAL DE TODAS AS GERAÇÕES (PLAYSTATION, NINTENDO, SEGA, XBOX)
# =======================================================
import urllib.request
import json
import urllib.parse


def consultar_ia_historica(jogo_escolhido):
    print(f"\n🤖 [GAMEHUB AI]: Vasculhando registros históricos de todos os consoles por '{jogo_escolhido}'...")

    try:
        # Formata o termo de busca para a API da Wikipedia em português
        termo_busca = jogo_escolhido.strip() + " (jogo eletrônico)"
        url_base = "https://wikipedia.org"
        url_busca = f"{url_base}?action=query&list=search&srsearch={urllib.parse.quote(termo_busca)}&format=json"

        req = urllib.request.Request(url_busca, headers={'User-Agent': 'GameHubProductBot/1.0'})
        with urllib.request.urlopen(req) as response:
            dados_busca = json.loads(response.read().decode())

            if not dados_busca['query']['search']:
                # Se não achar com o sufixo, tenta busca genérica
                url_busca = f"{url_base}?action=query&list=search&srsearch={urllib.parse.quote(jogo_escolhido)}&format=json"
                req_gen = urllib.request.Request(url_busca, headers={'User-Agent': 'GameHubProductBot/1.0'})
                with urllib.request.urlopen(req_gen) as resp2:
                    dados_busca = json.loads(resp2.read().decode())

            if dados_busca['query']['search']:
                # Pega o título exato do artigo encontrado
                titulo_artigo = dados_busca['query']['search']['title']

                # Faz uma segunda chamada para pegar o resumo (sinopse) do artigo
                url_conteudo = f"{url_base}?action=query&prop=extracts&exintro&explaintext"
                url_conteudo += f"&titles={urllib.parse.quote(titulo_artigo)}&format=json"
                
                req_cont = urllib.request.Request(url_conteudo, headers={'User-Agent': 'GameHubProductBot/1.0'})
                with urllib.request.urlopen(req_cont) as resp_conteudo:
                    dados_conteudo = json.loads(resp_conteudo.read().decode())
                    paginas = dados_conteudo['query']['pages']
                    id_pagina = list(paginas.keys())
                    sinopse = paginas[id_pagina]['extract']

                    # Corta a sinopse se for longa demais para o terminal
                    if len(sinopse) > 400:
                        sinopse = sinopse[:400] + "..."

                    print("--------------------------------------------------")
                    print(f"🎮 TÍTULO OFICIAL: {titulo_artigo.replace(' (jogo eletrônico)', '')}")
                    print("📖 DETALHES HISTÓRICOS & SINOPSE:")
                    print(f"   {sinopse}")
                    print("--------------------------------------------------")
                    print("🤖 [DICA IA]: Você pode pesquisar clássicos de qualquer console:")
                    print("   'Super Mario World', 'Sonic Mega Drive', 'Halo Xbox' ou 'Zelda Switch'.")
                    print("--------------------------------------------------")
            else:
                print("❌ Jogo não localizado nos registros históricos da IA. Verifique o nome!")

    except Exception:
        print("⚠️ Erro de rede ou comunicação ao consultar a base de dados histórica.")


def iniciar_sistema():
    jogadores = []
    salas = []

    while True:
        print("\n==================================================")
        print("      BEM-VINDO AO GAMEHUB MATCHMAKER 🎮          ")
        print("==================================================")
        print("1. Cadastrar Jogador e Preferências de Jogos")
        print("2. Criar Sala de Partida Multiplayer / Co-op")
        print("3. Listar Salas e Jogadores Online")
        print("4. Perguntar para a IA (Busca Global - Todos os Consoles)")
        print("5. Sair do Sistema")
        print("==================================================")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            nome = input("Digite o nickname do jogador: ")
            jogo = input("Digite o seu jogo favorito: ")
            jogadores.append(f"{nome} ({jogo})")
            print(f"✅ Jogador {nome} cadastrado com sucesso!")

        elif opcao == "2":
            jogo_sala = input("Digite o nome do jogo para a sala: ")
            dono = input("Digite o seu nickname: ")
            salas.append(f"Sala de [{jogo_sala}] - Criada por: {dono}")
            print(f"🎮 Sala de {jogo_sala} aberta! Aguardando jogadores...")

        elif opcao == "3":
            print("\n--- STATUS ATUAL DO GAMEHUB ---")
            print(f"Jogadores Online: {jogadores if jogadores else 'Nenhum jogador cadastrado'}")
            print(f"Salas Ativas: {salas if salas else 'Nenhuma sala aberta'}")

        elif opcao == "4":
            print("Digite QUALQUER jogo da história (Ex: Super Mario World, Sonic Mega Drive, Halo, Zelda):")
            jogo_consulta = input("Nome do jogo: ")
            consultar_ia_historica(jogo_consulta)

        elif opcao == "5":
            print("Desconectando do GameHub... Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    iniciar_sistema()
