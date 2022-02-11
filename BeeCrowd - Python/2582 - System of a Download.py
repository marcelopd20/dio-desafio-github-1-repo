"""System of a Download é uma famosa banda de Hacker Metal! Certa vez, eles criaram um dispositivo, com seis botões,
numerados de 0 a 5, e colocaram nesse dispositivo os seus 11 maiores sucessos. Para tocar uma destas músicas, é preciso
pressionar dois botões. Com isso, os números destes dois botões são somados, e então toca-se a música correspondente ao
número da soma, conforme a relação abaixo:

0 - PROXYCITY
1 - P.Y.N.G.
2 - DNSUEY!
3 - SERVERS
4 - HOST!
5 - CRIPTONIZE
6 - OFFLINE DAY
7 - SALT
8 - ANSWER!
9 - RAR?
10 - WIFI ANTENNAS


Por exemplo, se os botões pressionados forem 3 e 4, irá tocar a música 7 - SALT
Escreva um programa que, dados os dois botões que forem pressionados, determine qual música irá tocar.

Entrada
Um número inteiro C será informado, que será a quantidade de casos de teste. Cada caso tem dois valores inteiros, X e Y,
representando quais botões foram pressionados.

Saída
Para cada caso de teste, imprima o nome da música correspondente."""
for c in range(int(input())):
    X = sum(int(x) for x in input().split())
    if X == 0:
        print('PROXYCITY')
    elif X == 1:
        print('P.Y.N.G.')
    elif X == 2:
        print('DNSUEY!')
    elif X == 3:
        print('SERVERS')
    elif X == 4:
        print('HOST!')
    elif X == 5:
        print('CRIPTONIZE')
    elif X == 6:
        print('OFFLINE DAY')
    elif X == 7:
        print('SALT')
    elif X == 8:
        print('ANSWER!')
    elif X == 9:
        print('RAR?')
    elif X == 10:
        print('WIFI ANTENNAS')