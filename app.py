# =======================================================
# PROJETO GAMEHUB - ENGENHARIA DE PRODUTO & IA DE GAMES
# BUSCA HISTÓRICA DESDE O PS1 ATÉ O PS5 (VIA WIKIPEDIA API)
# =======================================================
import urllib.request
import json
import urllib.parse
import re

def consultar_ia_historica(jogo_escolhido):
    print(f"\n🤖 [GAMEHUB AI]: Vasculhando registros históricos de PS1 a PS5 por '{jogo_escolhido}'...")
    
    try:
        # Formata o termo de busca para a API da Wikipedia em português
        termo_busca = jogo_escolhido.strip() + " (jogo eletrônico)"
        url_busca = f"https://wikipedia.org{urllib.parse.quote(termo_busca)}&format=json"
        
        req = urllib.request.Request(url_busca, headers={'User-Agent': 'GameHubProductBot/1.0'})
        with urllib.request.urlopen(req) as response:
            dados_busca = json.loads(response.read().decode())
            
            if not dados_busca['query']['search']:
                # Se não achar com o sufixo, tenta busca genérica
                url_busca = f"https://wikipedia.org{urllib.parse.quote(jogo_escolhido)}&format=json"
                with urllib.request.urlopen(urllib.request.Request(url_busca, headers={'User-Agent': 'GameHubProductBot/1.0'})) as resp2:
                    dados_busca = json.loads(resp2.read().decode())

            if dados_busca['query']['search']:
                # Pega o título exato do artigo encontrado
                titulo_artigo = dados_busca['query']['search'][0]['title']
                
                # Faz uma segunda chamada para pegar o resumo (sinopse) do artigo
                url_conteudo = f"https://wikipedia.org{urllib.parse.quote(titulo_artigo)}&format=json"
                with urllib.request.urlopen(urllib.request.Request(url_conteudo, headers={'User-Agent': 'GameHubProductBot/1.0'})) as resp_conteudo:
                    dados_conteudo = json.loads(resp_conteudo.read().decode())
                    paginas = dados_conteudo['query']['pages']
                    id_pagina = list(paginas.keys())[0]
                    sinopse = paginas[id_pagina]['extract']
                    
                    # Corta a sinopse se for longa demais para o terminal
                    if len(sinopse) > 400:
                        sinopse = sinopse[:400] + "..."

                    print("--------------------------------------------------")
                    print(f"🎮 TÍTULO OFICIAL: {titulo_artigo.replace(' (jogo eletrônico)', '')}")
                    print(f"📖 DETALHES HISTÓRICOS & SINOPSE:")
                    print(f"   {sinopse}")
                    print("--------------------------------------------------")
                    print("🤖 [DICA IA]: Você pode pesquisar clássicos como 'Silent Hill PS1',")
                    print("   'gta san andreas', 'God of War 3' ou 'God of War Ragnarok'.")
                    print("--------------------------------------------------")
            else:
                print("❌ Jogo não localizado nos registros históricos da IA. Verifique o nome!")
                
    except Exception as e:
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
        print("4. Perguntar para a IA (Busca Histórica PS1 ao PS5)")
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
            jogo_consulta = input("Digite QUALQUER jogo (Ex: Resident Evil 3, Shadow of the Colossus, Infamous, Spider-Man 2): ")
            consultar_ia_historica(jogo_consulta)
            
        elif opcao == "5":
            print("Desconectando do GameHub... Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    iniciar_sistema()
