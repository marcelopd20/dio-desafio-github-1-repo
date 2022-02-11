"""Faça um programa que leia um valor T e preencha um vetor N[1000] com a sequência de valores de 0 até
T-1 repetidas vezes, conforme exemplo abaixo. Imprima o vetor N.
Entrada
A entrada contém um valor inteiro T (2 ≤ T ≤ 50).
Saída
Para cada posição do vetor, escreva "N[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela
posição.Faça um programa que leia um valor T e preencha um vetor
N[1000] com a sequência de valores de 0 até T-1 repetidas vezes, conforme exemplo abaixo. Imprima o vetor N."""
T = int(input())
lis = list()
b = 0
while len(lis) <= 999:
    for c in range(0, (T if 2 <= T <= 50 else exit())):
        if len(lis) <= 999:
            lis.append(c)
        else:
            break
for i, v in enumerate(lis):
    print(f'N[{i}] = {v}')
