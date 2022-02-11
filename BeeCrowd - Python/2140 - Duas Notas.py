"""Gilberto é um famoso vendedor de esfirras na região. Porém, apesar de todos gostarem de suas esfirras,
ele só sabe dar o troco com duas notas, ou seja, nem sempre é possível receber o troco certo. Para facilitar a
vida de Gil, escreva um programa para ele que determine se é possível ou não devolver o troco exato utilizando
duas notas.

As notas disponíveis são: 2, 5, 10, 20, 50 e 100.

Entrada
A entrada deve conter o valor inteiro N da compra realizada pelo cliente e, em seguida, o valor inteiro M pago
pelo cliente (N < M ≤ 104). A entrada termina com N = M = 0.

Saída
Seu programa deverá imprimir "possible" se for possível devolver o troco exato ou "impossible" se não for possível."""
# este código serve para o uri, mas apresenta erros,
S = [2, 5, 10, 20, 50, 100]
while True:
    N, M = map(int, input().split())
    if N == 0 == M:
        break
    M -= N
    L = 0
    for c in S:
        if M == c * 2:
            L = 2

    for c in range(5, -1, -1):
        if M - S[c] >= 0:
            M -= S[c]
            L += 1
    if L == 2:
        P = 'possible'
    else:
        P = 'impossible'
    print(P)
