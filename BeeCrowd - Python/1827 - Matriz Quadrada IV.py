"""Neste programa seu trabalho é ler um valor inteiro que será o tamanho da matriz quadrada
(largura e altura) que será preenchida da seguinte forma: a parte externa é preenchida com 0, a parte
interna é preenchida com 1, a diagonal principal é preenchida com 2, a diagonal secundária é preenchida
com 3 e o ponto central contém o valor 4, conforme os exemplos abaixo.

Obs: o quadrado com '1' sempre começa na posição tamanho/3, tanto na largura quanto quanto na altura. A
linha e a coluna começam em zero (0).

Entrada
A entrada contém vários casos de teste e termina com EOF (fim de arquivo. Cada caso de teste consiste de
um valor inteiro ímpar N (5 ≤ N ≤ 101) que é o tamanho da matriz.

Saída
Para cada caso de teste, imprima a matriz correspondente conforme o exemplo abaixo. Após cada caso de
teste, imprima uma linha em branco."""
while True:
    try:
        N = int(input())
        for l in range(N):
            for c in range(N):
                if c == (N // 2) and l== (N // 2):
                    a = 4
                elif c >= ((N//3)) and c <= (N - (N//3) -1) and l >= ((N//3)) and l <= (N -(N//3) -1):
                    a = 1
                elif l == (N - 1) - c:
                    a = 3
                elif c == l:
                    a = 2
                else:
                    a = 0
                print(a, end='')
            print('')
        print('')
    except EOFError:
        break