import numpy as np

def colocar_peca(tabuleiro, linha, coluna, peca):
    tabuleiro[linha][coluna] = peca

def verifica_vitoria(tabuleiro, peca):
    linhas = np.any(np.all(tabuleiro == peca, axis=1))
    colunas = np.any(np.all(tabuleiro == peca, axis=0))
    diagonais = np.all(np.diag(tabuleiro == peca)) or np.all(np.diag(np.fliplr(tabuleiro)) == peca)
    return linhas or colunas or diagonais

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(str(x) if x != 0 else " " for x in linha))
        print("-" * 8)

def jogo():
    tabuleiro = np.zeros((3,3), dtype=int)
    peca_atual = 1
    vencedor = False
    empate = False

    while not vencedor and not empate:
        imprimir_tabuleiro(tabuleiro)

        while True:
            try:
                linha = int(input(f"Jogador {peca_atual}, escolha a linha (0, 1, 2): "))
                coluna = int(input(f"Jogador {peca_atual}, escolha a coluna (0, 1, 2): "))

                if linha not in [0,1,2] or coluna not in [0,1,2]:
                    print("\nEscolha linhas e colunas válidas! De 0 a 2.\n")
                    continue

                if tabuleiro[linha][coluna] != 0:
                    print("\nPosição ocupada! Tente novamente.\n")
                    continue

                colocar_peca(tabuleiro, linha, coluna, peca_atual)
                break  # jogada válida, sai do loop interno

            except ValueError:
                print("\nEntrada inválida! Insira números inteiros de 0 a 2. \n")

        # verifica vitória/empate após jogada válida
        vencedor = verifica_vitoria(tabuleiro, peca_atual)
        if np.all(tabuleiro != 0) and not vencedor:
            empate = True

        # troca de jogador se o jogo continuar
        if not vencedor and not empate:
            peca_atual = 2 if peca_atual == 1 else 1

    # imprime o tabuleiro final
    imprimir_tabuleiro(tabuleiro)

    if vencedor:
        print(f"\n\n\tParabéns Jogador {peca_atual}, você venceu!!")
    else:
        print("\n\n\tO jogo acabou empatado.")

jogo()
