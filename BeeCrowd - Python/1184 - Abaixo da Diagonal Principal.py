"""Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12].
Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão abaixo da diagonal
principal da matriz, conforme ilustrado abaixo (área verde).
Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média)
que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.
Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal."""
O = str(input())
Col = list()
Lin = list()
s = 0
for l in range(12):
    for c in range(12):
        X = float(input())
        Col.append(X)
    Lin.append(Col.copy())
    Col.clear()
for l in range(12):
    for c in range(12):
        if l > c:
            s += Lin[l][c]
print(f'{s:.1f}') if O in 'Ss' else print(f'{s/66:.1f}')