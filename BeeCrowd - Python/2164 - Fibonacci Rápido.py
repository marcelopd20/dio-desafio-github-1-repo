"""A fórmula de Binet é uma forma de calcular números de Fibonacci.

Sua tarefa é, dado um natural n, calcular o valor de Fibonacci(n) usando a fórmula acima.

Entrada
A entrada é um número natural n (0 < n ≤ 50).

Saída
A saída é o valor de Fibonacci(n) com 1 casa decimal utilizando a fórmula de Binet dada."""


def Fib(f):
    return ((((1 + (5 ** (1 / 2))) / 2) ** f) - (((1 - (5 ** (1 / 2))) / 2) ** f)) / (5 ** (1 / 2))


print(f'{Fib(int(input(""))):.1f}')
