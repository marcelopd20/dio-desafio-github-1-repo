"""Leia um valor inteiro N que é o tamanho da matriz que deve ser impressa conforme o modelo fornecido.

Entrada
A entrada contém vários casos de teste e termina com EOF. Cada caso de teste é composto por um único inteiro N (3 ≤ N < 70),
que determina o tamanho (linhas e colunas) de uma matriz que deve ser impressa.

Saída
Para cada N lido, apresente a saída conforme o exemplo fornecido."""
while True:
    try:
        N = int(input())
        #Lin = []
        #Col = []

        for l in range(N):
#            b = 0
            for c in range(N):
                if l == (N-1) - c:
                   a = 2
                elif c == l:
                    a = 1
                else:
                    a = 3
                print(a, end='')
            print('')
    except EOFError:
        break
                #Col.append(a)
        #Lin.append(Col.copy())
        #Col.clear()
    #print(Lin)