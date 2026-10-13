# =======================================================
# PROJETO GAMEHUB - SISTEMA DE MATCHMAKING EVOLUÍDO (AC02)
# Disciplina: Software Product: Analysis, Specification, Project & Implementation
# =======================================================

class Jogador:
    def __init__(self, nickname, jogo_favorito):
        self.nickname = nickname
        self.jogo_favorito = jogo_favorito

    def __str__(self):
        return f"{self.nickname} (Jogo Favorito: {self.jogo_favorito})"


class Sala:
    def __init__(self, id_sala, jogo, dono):
        self.id_sala = id_sala
        self.jogo = jogo
        self.dono = dono
        self.jogadores = [dono]

    def adicionar_jogador(self, jogador):
        if jogador not in self.jogadores:
            self.jogadores.append(jogador)
            return True
        return False

    def __str__(self):
        membros = ", ".join([j.nickname for j in self.jogadores])
        return f"ID #{self.id_sala} | Jogo: [{self.jogo}] | Host: {self.dono.nickname} | Jogadores ({len(self.jogadores)}): [{membros}]"


def iniciar_sistema():
    jogadores = []
    salas = []
    contador_salas = 1

    while True:
        print("\n==================================================")
        print("      BEM-VINDO AO GAMEHUB MATCHMAKER v2.0 🎮     ")
        print("==================================================")
        print("1. Cadastrar Jogador e Preferências")
        print("2. Criar Sala de Partida Online")
        print("3. Executar Matchmaking Automático ⚡ (NOVO)")
        print("4. Entrar em uma Sala Existente 👥 (NOVO)")
        print("5. Listar Salas e Jogadores Ativos")
        print("6. Sair do Sistema")
        print("==================================================")

        opcao = input("Escolha uma opção (1-6): ").strip()

        if opcao == "1":
            nome = input("Digite o nickname do jogador: ").strip()
            jogo = input("Digite o seu jogo favorito: ").strip()
            
            if nome and jogo:
                novo_jogador = Jogador(nome, jogo)
                jogadores.append(novo_jogador)
                print(f"✅ Jogador '{nome}' cadastrado com sucesso!")
            else:
                print("❌ Nome e Jogo não podem ser vazios.")

        elif opcao == "2":
            if not jogadores:
                print("❌ Cadastre pelo menos um jogador antes de criar uma sala.")
                continue

            print("\nJogadores disponíveis para criar a sala:")
            for idx, j in enumerate(jogadores, 1):
                print(f"  {idx}. {j.nickname}")
            
            try:
                escolha_host = int(input("Escolha o número do jogador host: ")) - 1
                if 0 <= escolha_host < len(jogadores):
                    host = jogadores[escolha_host]
                    jogo_sala = input(f"Jogo da sala (Padrão: {host.jogo_favorito}): ").strip()
                    if not jogo_sala:
                        jogo_sala = host.jogo_favorito

                    nova_sala = Sala(contador_salas, jogo_sala, host)
                    salas.append(nova_sala)
                    contador_salas += 1
                    print(f"🎮 Sala #{nova_sala.id_sala} de [{jogo_sala}] criada por {host.nickname}!")
                else:
                    print("❌ Opção de jogador inválida.")
            except ValueError:
                print("❌ Digite um número válido.")

        elif opcao == "3":
            print("\n⚡ --- MATCHMAKING AUTOMÁTICO ---")
            if not salas:
                print("❌ Nenhuma sala disponível para matchmaking.")
                continue

            encontrou_match = False
            for sala in salas:
                # Procura jogadores cadastrados que gostam do jogo da sala e ainda não estão nela
                for j in jogadores:
                    if j.jogo_favorito.lower() == sala.jogo.lower() and j not in sala.jogadores:
                        sala.adicionar_jogador(j)
                        print(f"🎯 MATCH! Jogador '{j.nickname}' foi adicionado automaticamente à Sala #{sala.id_sala} [{sala.jogo}]!")
                        encontrou_match = True

            if not encontrou_match:
                print("ℹ️ Nenhum novo compatível encontrado para as salas ativas.")

        elif opcao == "4":
            if not salas or not jogadores:
                print("❌ É necessário ter ao menos 1 sala e 1 jogador para esta funcionalidade.")
                continue

            print("\nSalas Disponíveis:")
            for s in salas:
                print(f"  {s}")

            try:
                id_busca = int(input("Digite o ID da sala onde deseja entrar: "))
                sala_encontrada = next((s for s in salas if s.id_sala == id_busca), None)

                if sala_encontrada:
                    print("\nSelecione o jogador:")
                    for idx, j in enumerate(jogadores, 1):
                        print(f"  {idx}. {j.nickname}")
                    
                    idx_j = int(input("Número do jogador: ")) - 1
                    if 0 <= idx_j < len(jogadores):
                        jogador_add = jogadores[idx_j]
                        if sala_encontrada.adicionar_jogador(jogador_add):
                            print(f"✅ {jogador_add.nickname} entrou na Sala #{sala_encontrada.id_sala}!")
                        else:
                            print("⚠️ Jogador já está nesta sala.")
                    else:
                        print("❌ Jogador inválido.")
                else:
                    print("❌ Sala não encontrada.")
            except ValueError:
                print("❌ Entrada inválida.")

        elif opcao == "5":
            print("\n--- STATUS ATUAL DO GAMEHUB ---")
            print("Jogadores Cadastrados:")
            if jogadores:
                for j in jogadores:
                    print(f"  • {j}")
            else:
                print("  Nenhum jogador cadastrado.")

            print("\nSalas Ativas:")
            if salas:
                for s in salas:
                    print(f"  • {s}")
            else:
                print("  Nenhuma sala aberta.")

        elif opcao == "6":
            print("Desconectando do GameHub v2.0... Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    iniciar_sistema() 
