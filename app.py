# =======================================================
# PROJETO GAMEHUB - IA COM ESPECIFICAÇÃO DE JOGOS (API)
# =======================================================
import urllib.request
import json
import urllib.parse

# Banco de dados local com as especificações detalhadas de cada GTA e outros mundos abertos
BANCO_IA_LOCAL = {
    "gta 5": {
        "nome": "Grand Theft Auto V",
        "empresa": "Rockstar Games",
        "plataformas": "PS3, PS4, PS5, Xbox 360, Xbox One, Xbox Series X/S, PC",
        "classificacao": "18+ (Inadequado para menores de 18 anos)",
        "sinopse": "Um malandro de rua, um ladrão de bancos aposentado e um psicopata se envolvem com o submundo do crime em Los Santos."
    },
    "gta 4": {
        "nome": "Grand Theft Auto IV",
        "empresa": "Rockstar Games",
        "plataformas": "PS3, Xbox 360, PC",
        "classificacao": "18+ (Inadequado para menores de 18 anos)",
        "sinopse": "O imigrante Niko Bellic chega em Liberty City para viver o 'Sonho Americano' e escapar de seu passado sombrio."
    },
    "gta san andreas": {
        "nome": "Grand Theft Auto: San Andreas",
        "empresa": "Rockstar Games",
        "plataformas": "PS2, PS3, PS4, Xbox, Xbox 360, Xbox One, PC, Android, iOS",
        "classificacao": "18+ (Inadequado para menores de 18 anos)",
        "sinopse": "Carl Johnson (CJ) retorna para o seu bairro natal em Los Santos após o assassinato de sua mãe e precisa reerguer sua gangue."
    },
    "gta vice city": {
        "nome": "Grand Theft Auto: Vice City",
        "empresa": "Rockstar Games",
        "plataformas": "PS2, PS3, Xbox, PC, Android, iOS",
        "classificacao": "18+ (Inadequado para menores de 18 anos)",
        "sinopse": "Nos anos 80, Tommy Vercetti é enviado para Vice City após sair da prisão e constrói seu próprio império criminoso na cidade."
    },
    "red dead redemption": {
        "nome": "Red Dead Redemption 2",
        "empresa": "Rockstar Games",
        "plataformas": "PS4, Xbox One, PC",
        "classificacao": "18+ (Inadequado para menores de 18 anos)",
        "sinopse": "Arthur Morgan e a gangue Van der Linde fogem de agentes federais no fim da era do Velho Oeste."
    },
    "skyrim": {
        "nome": "The Elder Scrolls V: Skyrim",
        "empresa": "Bethesda Game Studios",
        "plataformas": "PS5, Xbox Series X/S, Nintendo Switch, PC, PS4",
        "classificacao": "16+ (Inadequado para menores de 16 anos)",
        "sinopse": "O herói Dragonborn deve derrotar Alduin, um dragão profetizado a destruir o mundo."
    },
    "cyberpunk": {
        "nome": "Cyberpunk 2077",
        "empresa": "CD Projekt RED",
        "plataformas": "PC, PS5, Xbox Series X/S, PS4, Xbox One",
        "classificacao": "18+ (Inadequado para menores de 18 anos)",
        "sinopse": "Um RPG de ação em Night City, uma megalópole obcecada por poder, glamour e modificações corporais."
    },
    "far cry 3": {
        "nome": "Far Cry 3",
        "empresa": "Ubisoft",
        "plataformas": "PC, PS3, Xbox 360, PS4, Xbox One",
        "classificacao": "18+ (Inadequado para menores de 18 anos)",
        "sinopse": "Jason Brody deve resgatar seus amigos sequestrados por piratas em uma ilha isolada comandada por Vaas Montenegro."
    }
}

def consultar_ia(jogo_escolhido):
    busca = jogo_escolhido.lower().strip()
    
    # 1. Verifica se o nome digitado bate exatamente com uma das chaves locais
    if busca in BANCO_IA_LOCAL:
        info = BANCO_IA_LOCAL[busca]
        print("\n🤖 [GAMEHUB AI]: Processando informações locais do jogo...")
        print("--------------------------------------------------")
        print(f"🎮 TÍTULO: {info['nome']}")
        print(f"🏢 EMPRESA: {info['empresa']}")
        print(f"🖥️ PLATAFORMAS: {info['plataformas']}")
        print(f"🔞 CLASSIFICAÇÃO: {info['classificacao']}")
        print(f"📖 SINOPSE: {info['sinopse']}")
        print("--------------------------------------------------")
        return

    # 2. Se não for um dos GTAs ou jogos específicos listados, faz a busca global na internet
    print(f"\n🤖 [GAMEHUB AI]: Procurando '{jogo_escolhido}' na base de dados global pública...")
    try:
        nome_url = urllib.parse.quote(jogo_escolhido)
        url = f"https://cheapshark.com{nome_url}"
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            dados = json.loads(response.read().decode())
            
            if dados:
                jogo_encontrado = dados[0]
                print("--------------------------------------------------")
                print(f"🎮 TÍTULO ENCONTRADO: {jogo_encontrado['external']}")
                print(f"🆔 ID GLOBAL DO GAME: {jogo_encontrado['gameID']}")
                print(f"💵 MELHOR PREÇO ATUAL: ${jogo_encontrado['cheapest']} USD")
                print(f"🖼️ LINK DA CAPA: https://cheapshark.com{jogo_encontrado['gameID']}.jpg")
                print("ℹ️ Nota: Sinopse disponível apenas para os jogos principais catalogados localmente.")
                print("--------------------------------------------------")
            else:
                print("❌ Jogo não encontrado na base de dados global. Verifique a grafia!")
    except Exception as e:
        print("⚠️ Erro de conexão ao buscar na base global de jogos.")

def iniciar_sistema():
    jogadores = []
    salas = []
    
    while True:
        print("\n==================================================")
        print("      BEM-VINDO AO GAMEHUB MATCHMAKER 🎮          ")
        print("==================================================")
        print("1. Cadastrar Jogador e Preferências de Jogos")
        print("2. Criar Sala de Partida/Co-op")
        print("3. Listar Salas e Jogadores Online")
        print("4. Perguntar para a IA do GameHub (Busca Específica/Global)")
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
            jogo_consulta = input("Digite o jogo (ex: gta 5, gta vice city, cyberpunk, minecraft): ")
            consultar_ia(jogo_consulta)
            
        elif opcao == "5":
            print("Desconectando do GameHub... Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    iniciar_sistema()
