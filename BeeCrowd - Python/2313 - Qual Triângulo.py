"""Dados três valores, verifique se os três podem formar um triângulo. Em caso afirmativo, verifique se ele é escaleno,
isóceles ou equilátero e se trata-se de um triângulo retângulo ou não.

Entrada
A entrada consiste em três números inteiros A,B e C (0 < A,B,C < 105).

Saída
A saída deve conter a string "Invalido" se os valores lidos não formarem um triângulo. Se os valores formarem um
triângulo a saída deve ser "Valido-Equilatero", "Valido-Escaleno" ou "Valido-Isoceles" de acordo com a característica
do triângulo seguido de "Retangulo: S" se o triângulo for retângulo ou "Retangulo: N" se não for, conforme os exemplos."""
t = list(map(int, input().split()))
t.sort()
if (t[0] + t[1]) <= t[2]:
    print('Invalido')
else:
    if t[0] == t[1] == t[2]:
        print('Valido-Equilatero')
    elif t[0] == t[1] != t[2] or t[0] == t[2] != t[1] or t[1] == t[2] != t[0]:
        print('Valido-Isoceles')
    else:
        print('Valido-Escaleno')
    [print(f'Retangulo: S') if (t[0]**2) + (t[1]**2) == (t[2]**2) else print('Retangulo: N')]

