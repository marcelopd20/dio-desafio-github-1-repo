"""Está chegando a grande final do Campeonato Nlogonense de Surf Aquático, que este ano ocorrerá na cidade de Bonita
Horeleninha (BH)! Nesta cidade, o jogo PãodeQueijoSweeper é bastante popular!

O tabuleiro do jogo consiste em uma matriz de N linhas e M colunas. Cada célula da matriz contém um pão de queijo ou o
número de pães de queijo que existem nas celulas adjacentes a ela. Uma célula é adjacente a outra se estiver
imediatamente à esquerda, à direita, acima ou abaixo da célula. Note que, se não contiver um pão de queijo, uma célula
deve obrigatoriamente conter um número entre 0 e 4, inclusive.

Dadas as posições dos pães de queijo, determine o tabuleiro do jogo!

Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso contém os inteiros N e M (1 ≤ N, M ≤ 100).
As próximas N linhas contém M inteiros cada, separados por espaços, descrevendo os pães de queijo no tabuleiro.
O j-ésimo inteiro da i-ésima linha é 1 se existe um pão de queijo na linha i e coluna j do tabuleiro, ou 0 caso
contrário.

A entrada termina com fim-de-arquivo (EOF).

Saída
Para cada caso de teste, imprima N linhas com M inteiros cada, não separados por espaços, descrevendo a configuração do
tabuleiro. Se uma posição contém um pão de queijo, imprima 9 para ela; caso contrário, imprima o número cuja posição
deve conter."""
while True:
    try:
        mat = list()
        s = list()
        N, M = (int(x) for x in input().split())
        for n in range(N):
            mat.append(list(map(int, input().split()))[:M])
            for m in range(M):
                if mat[n][m] == 1:
                    mat[n][m] = 9
        for i in range(len(mat)):
            for t in range(len(mat[i])):
                if mat[i][t] == 9:
                    if i > 0:
                        if mat[i-1][t] != 9:
                            mat[i-1][t] += 1
                    if i < N-1:
                        if mat[i + 1][t] != 9:
                            mat[i + 1][t] += 1
                    if t > 0:
                        if mat[i][t-1] != 9:
                            mat[i][t-1] += 1
                    if t < M-1:
                        if mat[i][t+1] != 9:
                            mat[i][t+1] += 1
        for i in range(len(mat)):
            for c, v in enumerate(mat[i]):
                print(v, end='')
            print()
    except EOFError:
        break