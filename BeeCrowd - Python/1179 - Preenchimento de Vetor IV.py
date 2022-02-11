''' Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares
ou ímpares. Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores
ncher, você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos.
Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os
valores do vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.'''
par = list()
impar = list()
for c in range(15):
    N = int(input())
    par.append(N) if N % 2 == 0 else impar.append(N)
    if len(par) == 5:
        for i, v in enumerate(par):
            print(f'par[{i}] = {v}')
        par.clear()
    elif len(impar) == 5:
        for i, v in enumerate(impar):
            print(f'impar[{i}] = {v}')
        impar.clear()
for i, v in enumerate(impar):
    print(f'impar[{i}] = {v}')
for i,v in enumerate(par):
    print(f'par[{i}] = {v}')