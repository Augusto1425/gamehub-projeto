# =======================================================
# PROJETO GAMEHUB - SISTEMA DE MATCHMAKING PARA GAMES
# =======================================================

def iniciar_sistema():
    jogadores = []
    salas = []
    
    while True:
        print("\n==================================================")
        print("      BEM-VINDO AO GAMEHUB MATCHMAKER 🎮          ")
        print("==================================================")
        print("1. Cadastrar Jogador e Preferências de Jogos")
        print("2. Criar Sala de Partida (Valorant, LoL, CS)")
        print("3. Listar Salas e Jogadores Online")
        print("4. Sair do Sistema")
        print("==================================================")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            nome = input("Digite o nickname do jogador: ")
            jogo = input("Digite o seu jogo favorito: ")
            jogadores.append(f"{nome} ({jogo})")
            print(f"✅ Jogador {nome} cadastrado com sucesso!")
            
        elif opcao == "2":
            jogo_sala = input("Para qual jogo deseja criar a sala? (Valorant/LoL/CS): ")
            dono = input("Digite o seu nickname: ")
            salas.append(f"Sala de {jogo_sala} - Criada por: {dono}")
            print(f"🎮 Sala de {jogo_sala} aberta! Aguardando jogadores...")
            
        elif opcao == "3":
            print("\n--- STATUS ATUAL DO GAMEHUB ---")
            print(f"Jogadores Online: {jogadores if jogadores else 'Nenhum jogador cadastrado'}")
            print(f"Salas Ativas: {salas if salas else 'Nenhuma sala aberta'}")
            
        elif opcao == "4":
            print("Desconectando do GameHub... Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    iniciar_sistema()
