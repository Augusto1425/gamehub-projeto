# =======================================================
# PROJETO GAMEHUB - ENGENHARIA DE PRODUTO & IA DE GAMES
# BUSCA GLOBAL PROTEGIDA CONTRA ERROS DE CONEXÃO (TODOS OS CONSOLES)
# =======================================================
import urllib.request
import json
import urllib.parse

# Banco de dados local 100% seguro para evitar quedas de rede no seu vídeo
BANCO_IA_LOCAL = {
    "gta 5": {
        "nome": "Grand Theft Auto V",
        "empresa": "Rockstar Games",
        "plataformas": "PS3, PS4, PS5, Xbox 360, Xbox One, Xbox Series X/S, PC",
        "sinopse": "Três criminosos totalmente diferentes alinham seus objetivos em Los Santos para aplicar grandes golpes."
    },
    "gta san andreas": {
        "nome": "Grand Theft Auto: San Andreas",
        "empresa": "Rockstar Games",
        "plataformas": "PS2, PS3, Xbox, Xbox 360, PC, Android, iOS",
        "sinopse": "Carl Johnson (CJ) precisa salvar sua família e tomar o controle das ruas do estado fictício de San Andreas."
    },
    "manhunt 2": {
        "nome": "Manhunt 2",
        "empresa": "Rockstar Games",
        "plataformas": "PS2, PSP, Nintendo Wii, PC",
        "sinopse": "Um experimento secreto em um laboratório de asilo mental dá terrivelmente errado, liberando uma caçada humana violenta."
    },
    "postal 2": {
        "nome": "Postal 2",
        "empresa": "Running With Scissors",
        "plataformas": "PC (Windows, Linux, macOS)",
        "sinopse": "Acompanhe uma semana bizarra na vida do Postal Dude, realizando tarefas diárias simples que sempre saem do controle."
    },
    "god of war": {
        "nome": "God of War (Série)",
        "empresa": "Santa Monica Studio",
        "plataformas": "PlayStation 2, PS3, PS4, PS5, PC",
        "sinopse": "A jornada mitológica de Kratos, o Fantasma de Esparta, contra os deuses olímpicos e nórdicos."
    },
    "super mario world": {
        "nome": "Super Mario World",
        "empresa": "Nintendo",
        "plataformas": "Super Nintendo (SNES), Game Boy Advance, Virtual Console",
        "sinopse": "Mario e Luigi precisam salvar a Princesa Peach e a Ilha dos Dinossauros das garras do vilão Bowser."
    }
}


def consultar_ia_historica(jogo_escolhido):
    busca = jogo_escolhido.lower().strip()

    # 1. Tenta ler direto do banco local seguro (Proteção contra quedas de API)
    if busca in BANCO_IA_LOCAL:
        info = BANCO_IA_LOCAL[busca]
        print("\n🤖 [GAMEHUB AI]: Processando informações locais com sucesso...")
        print("--------------------------------------------------")
        print(f"🎮 TÍTULO OFICIAL: {info['nome']}")
        print(f"🏢 EMPRESA: {info['empresa']}")
        print(f"🖥️ PLATAFORMAS: {info['plataformas']}")
        print(f"📖 SINOPSE HISTÓRICA: {info['sinopse']}")
        print("--------------------------------------------------")
        return

    # 2. Se for outro jogo aleatório, usa a busca global da internet
    print(f"\n🤖 [GAMEHUB AI]: Consultando registros externos por '{jogo_escolhido}'...")
    try:
        termo_busca = jogo_escolhido.strip() + " (jogo eletrônico)"
        url_base = "https://pt.wikipedia.org/w/api.php"
        url_busca = f"{url_base}?action=query&list=search&srsearch={urllib.parse.quote(termo_busca)}&format=json"

        # User-Agent modificado para o servidor da Wikipedia não bloquear a chamada
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) GameHubProductBot/1.0'}
        req = urllib.request.Request(url_busca, headers=headers)
        
        with urllib.request.urlopen(req) as response:
            dados_busca = json.loads(response.read().decode())

            if dados_busca['query']['search']:
                titulo_artigo = dados_busca['query']['search'][0]['title']

                url_conteudo = f"{url_base}?action=query&prop=extracts&exintro&explaintext"
                url_conteudo += f"&titles={urllib.parse.quote(titulo_artigo)}&format=json"
                
                req_cont = urllib.request.Request(url_conteudo, headers=headers)
                with urllib.request.urlopen(req_cont) as resp_conteudo:
                    paginas = json.loads(resp_conteudo.read().decode())['query']['pages']
                    sinopse = paginas[list(paginas.keys())[0]]['extract']

                    if len(sinopse) > 400:
                        sinopse = sinopse[:400] + "..."

                    print("--------------------------------------------------")
                    print(f"🎮 TÍTULO ENCONTRADO: {titulo_artigo.replace(' (jogo eletrônico)', '')}")
                    print(f"📖 RESUMO DA BASE GLOBAL:\n   {sinopse}")
                    print("--------------------------------------------------")
                    return
            print("❌ Jogo não localizado nos registros globais. Verifique a grafia!")

    except Exception:
        print("⚠️ Erro temporário de comunicação externa. Use os títulos sugeridos do menu!")


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
        print("4. Perguntar para a IA (Manhunt 2, Postal 2, GTA 5, Mario...)")
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
            print("Digite um jogo (Sugestões seguras: manhunt 2, postal 2, gta 5, super mario world):")
            jogo_consulta = input("Nome do jogo: ")
            consultar_ia_historica(jogo_consulta)

        elif opcao == "5":
            print("Desconectando do GameHub... Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    iniciar_sistema()
