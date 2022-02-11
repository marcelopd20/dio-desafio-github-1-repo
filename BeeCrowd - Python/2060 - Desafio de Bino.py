"""Bino e Cino são colegas inseparáveis. Bino gosta de criar desafios matemáticos para Cino resolver.
Desta vez, Bino gerou uma lista de números e perguntou ao Cino quantos números da lista são múltiplos de
2, 3, 4 e 5.

Esse desafio pode parecer simples, porém, quando a lista contém muitos números, Cino se confunde e acaba
errando alguns cálculos. Para ajudar Cino, faça um programa para resolver o desafio de Bino.

Entrada
A primeira linha da entrada consiste em um inteiro N (1 ≤ N ≤1000), representando a quantidade de números
na lista de Bino.

A segunda linha contém N inteiros Li (1 ≤ Li ≤ 100), representando os números da lista de Bino.

Saída
Imprima a quantidade de números múltiplos de 2, 3, 4 e 5 presentes na lista. Observe a formatação da
saída nos exemplos, pois ela deve ser seguida rigorosamente."""
N = int(input())
L = list(map(int, input().split()))[:N]
M2, M3, M4, M5 = [int(0) for c in range(4)]
for v in L:
    if v % 2 == 0:
        M2 += 1
    if v % 3 == 0:
        M3 += 1
    if v % 4 == 0:
        M4 += 1
    if v % 5 == 0:
        M5 += 1
print(f"{M2} Multiplo(s) de 2\n"
f"{M3} Multiplo(s) de 3\n"
f"{M4} Multiplo(s) de 4\n"
f"{M5} Multiplo(s) de 5")
