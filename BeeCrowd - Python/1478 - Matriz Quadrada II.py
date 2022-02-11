"""Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, e construa a matriz de
acordo com o exemplo abaixo.

Entrada
A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. O final da entrada
é marcado por um valor de ordem igual a zero (0).

Saída
Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. (os valores das matrizes devem ser formatados em
um campo de tamanho 3 justificados à direita e separados por espaço. Após o último caractere de cada linha da matriz não deve haver
espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco."""
while True:
    Lin = list()
    N = int(input())
    if N == 0:
        break
    for l in range(N):
        Col = list()
        for c in range(N):
            Col.append(1)
        Lin.append(Col.copy())
        Col.clear()
    for a in range(N):
        for l in range(N):
            for c in range(N):
                if l == c + a or l == c - a:
                    Lin[l][c] += a
    for l in range(N):
        imp = ''
        for c in range(N):
            imp += f' {Lin[l][c]:>3}'
        print(imp[1:])
    print('')
