"""Hyam é um menino que adora sequências. Ele anda descobrindo sequências interessantes que nem mesmo
Fibonacci imaginaria. Certo dia, Hyam percebeu que dado um número N, ele poderia fazer uma sequência do tipo
0 1 2 2 3 3 3 4 4 4 4 ... N N N ... N. No entanto, Hyam percebeu que cada valor que aumentava no número da sequência,
a quantidade total de números da sequência aumentava semelhantemente à um crescimento fatorial, neste caso,
ao invés de multiplicar, soma-se o número total de números da sequência com o valor do próximo número da sequência.
Por exemplo, se N = 2. A sequência correta seria 0 1 2 2, obtendo-se 4 digitos. Agora, se N = 3, o próximo número da
sequência tem valor 3, então a quantidade total de número da sequência seria a quantidade de números com N = 2,
que é 4, mais o valor do próximo número da sequência, neste caso 3, obtendo-se 7, já que a sequência correta para
N = 3 é 0 1 2 2 3 3 3.

Sua tarefa é fazer um algoritmo que dado um número inteiro N, tenha como resposta a quantidade total de números
dessa sequência e logo abaixo a sequência completa.

Entrada
A entrada é composta de vários casos de testes. Cada caso é composto por um inteiro N (0<=N<=200) que indica o valor
dos últimos N números da sequência.

A entrada termina com final de arquivo (EOF).

Saída
A saida é no formato Caso X: N numeros onde X é a ordem do número de casos e N é a quantidade de numeros que contém
na sequência completa, na próxima linha a sequência de números com um espaço entre eles. É pedido que deixe uma
linha em branco após cada caso."""
C = 1
while True:
    try:
        N = int(input())
        l = [int(n) for n in range(N+1) for c in range(n)]
        l.insert(0, 0)
        print(f'Caso {C}: {len(l)} {"numero" if len(l) == 1 else "numeros"}')
        for v in range(len(l)):
            print(f'{l[v]} 'if v < len(l)-1 else f'{l[v]}', end='')
        C += 1
        print('\n')
    except EOFError:
        break