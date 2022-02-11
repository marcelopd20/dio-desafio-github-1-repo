"""Ana e suas amigas estão fazendo um trabalho de geometria para o colégio, em que precisam formar vários
triângulos, numa cartolina, com algumas varetas de comprimentos diferentes. Logo elas perceberam que não dá para
formar triângulos com três varetas de comprimentos quaisquer: se uma das varetas for muito grande em relação às
outras duas, não dá para formar o triângulo.

Neste problema, você precisa ajudar Ana e suas amigas a determinar se, dados os comprimentos de quatro varetas, é ou
não é possível selecionar três varetas, dentre as quatro, e formar um triângulo.

Entrada
A entrada é composta por apenas uma linha contendo quatro números inteiros A, B, C e D (1 ≤ A, B, C, D ≤ 100).

Saída
Seu programa deve produzir apenas uma linha contendo apenas um caractere, que deve ser ‘S’ caso seja possível
formar o triângulo, ou ‘N’ caso não seja possível formar o triângulo."""
a, b, c, d = map(int, input().split())
if abs(a-b) < c < (a+b) \
        or abs(a-b) < d < (a+b) \
        or abs(a-c) < b < (a+c) \
        or abs(a-c) < d < (a+c) \
        or abs(a-d) < b < (a+d) \
        or abs(a-d) < c < (a+d) \
        or abs(b-c) < a < (b+c) \
        or abs(b-c) < d < (b+c) \
        or abs(b-d) < a < (b+d) \
        or abs(b-d) < c < (b+d) \
        or abs(c-d) < a < (c+d) \
        or abs(c-d) < b < (c+d):
    print('S')
else:
    print('N')
