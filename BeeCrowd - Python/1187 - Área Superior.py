"""Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a
média considerando somente aqueles elementos que estão na área superior da matriz, conforme ilustrado abaixo (área verde).

Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos
da matriz. Seguem 144 valores com ponto flutuante de dupla precisão que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal."""
O = str(input())
Col = []
Lin = []
s = 0
for l in range(12):
    for c in range(12):
        X = float(input())
        Col.append(X)
    Lin.append(Col.copy())
    Col.clear()
mai = 11
men = 1
d = 0
for l in range(0, 5):
    for c in range(men, mai):
        s += Lin[l][c]
        d += 1
    mai -= 1
    men += 1
print(f'{s:.1f}') if O in 'S' else print(f'{s/d:.1f}')