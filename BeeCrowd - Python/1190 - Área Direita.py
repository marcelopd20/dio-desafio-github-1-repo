"""Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule
e mostre a soma ou a média considerando somente aqueles elementos que estão na área direita da matriz, conforme ilustrado abaixo
(área verde).
Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser
realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal."""
O = input()
Col = list()
Lin = []
s = 0
for l in range(12):
    for c in range(12):
        X = float(input())
        Col.append(X)
    Lin.append(Col.copy())
    Col.clear()
minx = 5
maxx = 7
d = 0
for c in range(7, 12):
    for l in range(minx, maxx):
        s += Lin[l][c]
        d += 1
    minx -= 1
    maxx += 1
print(f'{s:.1f}') if O in 'S' else print(f'{s/d:.1f}')