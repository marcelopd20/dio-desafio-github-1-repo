"""Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou
a média considerando somente aqueles elementos que estão na área esquerda da matriz, conforme ilustrado abaixo (área verde).

Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os
elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal."""

O = str(input())
Col = list()
Lin = list()
for l in range(12):
    for c in range(12):
        X = float(input())
        Col.append(X)
    Lin.append(Col.copy())
    Col.clear()
s = 0
d = 0
minm = 1
maxm = 11
for c in range(0, 5):
    for l in range(minm, maxm):
        s += Lin[l][c]
        d += 1
    minm += 1
    maxm -= 1

print(f'{s:.1f}') if O in 'S' else print(f'{s/d:.1f}')
