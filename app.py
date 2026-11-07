# =======================================================
# PROJETO GAMEHUB - SISTEMA DE MATCHMAKING EVOLUÍDO (AC02)
# Disciplina: Software Product: Analysis, Specification, Project & Implementation
# =======================================================

import time

class Jogador:
    def __init__(self, nickname, jogo_favorito, elo="Ouro"):
        self.nickname = nickname
        self.jogo_favorito = jogo_favorito
        self.elo = elo  # 🌟 NOVO: Atributo de Balanceamento (Bronze, Prata, Ouro, Platina)

    def __str__(self):
        return f"{self.nickname} | Elo: [{self.elo}] | Jogo Favorito: {self.jogo_favorito}"


class Sala:
    def __init__(self, id_sala, jogo, dono, capacidade_max=4):
        self.id_sala = id_sala
        self.jogo = jogo
        self.dono = dono
        self.jogadores = [dono]
        self.capacidade_max = capacidade_max  # 🌟 NOVO: Limite de vagas
        self.status = "Aguardando Jogadores"  # 🌟 NOVO: Estado da sala (Aguardando ou Em Partida)

    def adicionar_jogador(self, jogador):
        if self.status == "Em Partida 🎮":
            return "partida_iniciada"
        if len(self.jogadores) >= self.capacidade_max:
            return "cheia"
        if jogador not in self.jogadores:
            self.jogadores.append(jogador)
            return "sucesso"
        return "ja_esta"

    def __str__(self):
        membros = ", ".join([f"{j.nickname}({j.elo})" for j in self.jogadores])
        status_vagas = f"({len(self.jogadores)}/{self.capacidade_max})"
        return f"ID #{self.id_sala} | Jogo: [{self.jogo}] | Status: [{self.status}] {status_vagas} | Host: {self.dono.nickname} | Time: [{membros}]"


def iniciar_sistema():
    jogadores = []
    salas = []
    contador_salas = 1

    # 🌟 Mock de dados iniciais para facilitar seu teste e gravação do vídeo!
    j1 = Jogador("Faker", "League of Legends", "Platina")
    j2 = Jogador("Sacy", "Valorant", "Platina")
    j3 = Jogador("Gaules", "CS2", "Ouro")
    j4 = Jogador("Nobru", "Free Fire", "Bronze")
    j5 = Jogador("Aspas", "Valorant", "Platina") # Compatível com o Sacy em elo e jogo!
    jogadores.extend([j1, j2, j3, j4, j5])

    while True:
        print("\n=======================================================")
        print("         BEM-VINDO AO GAMEHUB MATCHMAKER v3.0 🚀       ")
        print("=======================================================")
        print(" 1. Cadastrar Jogador e Rank (Elo)")
        print(" 2. Criar Sala de Partida Online")
        print(" 3. Executar Matchmaking Inteligente ⚡ (BALANCEADO)")
        print(" 4. Entrar / Gerenciar Sala Existente 👥")
        print(" 5. Listar Status do Servidor")
        print(" 6. Sair do Sistema")
        print("=======================================================")

        opcao = input("Escolha uma opção (1-6): ").strip()

        if opcao == "1":
            nome = input("Digite o nickname do jogador: ").strip()
            jogo = input("Digite o seu jogo favorito: ").strip()
            
            print("\nSelecione o nível de habilidade (Elo):")
            print("1. Bronze | 2. Prata | 3. Ouro | 4. Platina")
            elo_op = input("Opção (1-4): ").strip()
            elos = {"1": "Bronze", "2": "Prata", "3": "Ouro", "4": "Platina"}
            elo_selecionado = elos.get(elo_op, "Ouro")

            if nome and jogo:
                novo_jogador = Jogador(nome, jogo, elo_selecionado)
                jogadores.append(novo_jogador)
                print(f"✅ Jogador '{nome}' [{elo_selecionado}] cadastrado com sucesso!")
            else:
                print("❌ Nome e Jogo não podem ser vazios.")

        elif opcao == "2":
            if not jogadores:
                print("❌ Cadastre pelo menos um jogador antes de criar uma sala.")
                continue

            print("\nJogadores disponíveis para hospedar a sala:")
            for idx, j in enumerate(jogadores, 1):
                print(f"  {idx}. {j.nickname} (Fav: {j.jogo_favorito} | Elo: {j.elo})")
            
            try:
                escolha_host = int(input("Escolha o número do jogador host: ")) - 1
                if 0 <= escolha_host < len(jogadores):
                    host = jogadores[escolha_host]
                    jogo_sala = input(f"Jogo da sala (Padrão: {host.jogo_favorito}): ").strip()
                    if not jogo_sala:
                        jogo_sala = host.jogo_favorito

                    cap_max = input("Capacidade Máxima da Sala (Padrão: 4): ").strip()
                    cap_max = int(cap_max) if cap_max.isdigit() else 4

                    nova_sala = Sala(contador_salas, jogo_sala, host, cap_max)
                    salas.append(nova_sala)
                    contador_salas += 1
                    print(f"🎮 Sala #{nova_sala.id_sala} de [{jogo_sala}] criada com sucesso por {host.nickname}!")
                else:
                    print("❌ Opção de jogador inválida.")
            except ValueError:
                print("❌ Digite um número válido.")

        elif opcao == "3":
            print("\n⚡ --- PROCESSANDO MATCHMAKING INTELIGENTE DE PRODUTO ---")
            if not salas:
                print("❌ Nenhuma sala ativa disponível no servidor.")
                continue

            print("Buscando compatibilidades de Jogo + Habilidade (Elo)...")
            time.sleep(1) # Efeito estético para o seu vídeo parecer um processamento real
            encontrou_match = False

            for sala in salas:
                if sala.status == "Em Partida 🎮":
                    continue

                for j in jogadores:
                    # Regra de negócio de Produto: Só entra se for o mesmo jogo E o mesmo Elo do dono da sala
                    if (j.jogo_favorito.lower() == sala.jogo.lower() and 
                        j.elo.lower() == sala.dono.elo.lower() and 
                        j not in sala.jogadores):
                        
                        resultado = sala.adicionar_jogador(j)
                        if resultado == "sucesso":
                            print(f"🎯 MATCH BALANCED! '{j.nickname}' ({j.elo}) adicionado à Sala #{sala.id_sala} de [{sala.jogo}]!")
                            encontrou_match = True
                        elif resultado == "cheia":
                            print(f"⚠️ Sala #{sala.id_sala} atingiu o limite de capacidade e foi fechada!")
                            sala.status = "Em Partida 🎮"
                            break

            if not encontrou_match:
                print("ℹ️ Nenhum jogador com Elo e Jogo compatível pendente no momento.")

        elif opcao == "4":
            if not salas or not jogadores:
                print("❌ É necessário ter ao menos 1 sala e 1 jogador no sistema.")
                continue

            print("\nSalas Ativas Atualmente:")
            for s in salas:
                print(f"  {s}")

            try:
                id_busca = int(input("\nDigite o ID da sala para gerenciar: "))
                sala_encontrada = next((s for s in salas if s.id_sala == id_busca), None)

                if sala_encontrada:
                    print(f"\nGerenciando Sala #{sala_encontrada.id_sala}:")
                    print("1. Inserir um jogador manualmente")
                    print("2. Forçar Início da Partida (Mudar Status)")
                    sub_opcao = input("Escolha uma ação (1-2): ").strip()

                    if sub_opcao == "1":
                        print("\nSelecione o jogador para entrar:")
                        for idx, j in enumerate(jogadores, 1):
                            print(f"  {idx}. {j.nickname} ({j.elo})")
                        
                        idx_j = int(input("Número do jogador: ")) - 1
                        if 0 <= idx_j < len(jogadores):
                            jogador_add = jogadores[idx_j]
                            res = sala_encontrada.adicionar_jogador(jogador_add)
                            
                            if res == "sucesso":
                                print(f"✅ {jogador_add.nickname} entrou na Sala #{sala_encontrada.id_sala}!")
                            elif res == "ja_esta":
                                print("⚠️ Jogador já está nesta sala.")
                            elif res == "cheia":
                                print("❌ Não foi possível entrar. A sala está lotada!")
                            elif res == "partida_iniciada":
                                print("❌ A partida nesta sala já começou! Não são permitidos novos jogadores.")
                        else:
                            print("❌ Jogador inválido.")
                    
                    elif sub_opcao == "2":
                        if len(sala_encontrada.jogadores) >= 2:
                            sala_encontrada.status = "Em Partida 🎮"
                            print(f"🚀 Partida Iniciada! Sala #{sala_encontrada.id_sala} mudou o status para Em Partida.")
                        else:
                            print("❌ Não dá para iniciar uma partida com apenas 1 jogador na sala.")
                else:
                    print("❌ Sala não encontrada.")
            except ValueError:
                print("❌ Entrada inválida.")

        elif opcao == "5":
            print("\n================ STATS DO SERVIDOR ================")
            print("👥 JOGADORES LOGADOS:")
            if jogadores:
                for j in jogadores:
                    print(f"  • {j}")
            else:
                print("  Nenhum jogador cadastrado.")

            print("\n📡 LOBBIES / SALAS ATIVAS:")
            if salas:
                for s in salas:
                    print(f"  • {s}")
            else:
                print("  Nenhuma sala aberta.")
            print("===================================================\n")

        elif opcao == "6":
            print("Desconectando dos servidores do GameHub v3.0... Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    iniciar_sistema()
