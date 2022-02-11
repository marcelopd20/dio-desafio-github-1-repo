"""Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 15), correspondente a ordem de uma matriz
M de inteiros, e construa a matriz de acordo com o exemplo abaixo.

Entrada
A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem
construídas. O final da entrada é marcado por um valor de ordem igual a zero (0).

Saída
Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. Os valores das matrizes
devem ser formatados em um campo de tamanho T justificados à direita e separados por espaço, onde T é igual
ao número de dígitos do maior número da matriz. Após o último caractere de cada linha da matriz não deve
haver espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco."""
while True:
    Lin = []
    Col = []
    N = int(input())
    if N == 0:
        break
    for l in range(N):
        for c in range(N):
            Col.append(2**(l+c))
        Lin.append(Col.copy())
        Col.clear()
    T = len(str(Lin[N-1][N-1]))
    for l in range(N):
        imp = ''
        for c in range(N):
            imp += (f" {Lin[l][c]:>{T}}")
        print(imp[1:])
    print("")
