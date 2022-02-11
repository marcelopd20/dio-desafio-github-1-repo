"""Dados dois números naturais N1 e N2, diz-se que N1 é subsequência contígua de N2 se todos os dígitos de
N1 aparecem, na mesma ordem e de forma contígua, em N2. Crie uma aplicação que leia dois números naturais e
diga se o primeiro é uma subsequência contígua do segundo.

Entrada
A entrada é composta por vários casos de teste e termina com final de arquivo (EOF). A primeira linha de cada
entrada é composta por um valor natural N1(1 < N1 < 1010), a segunda linha é composta por um valor N2( N1 < N2 < 1032).

Saída
Para cada caso de teste imprima a quantidade de subsequências contíguas e a posição onde a subsequência é iniciada,
caso exista mais de uma subsequência, imprima onde é iniciada a última subsequência. Caso não exista subsequência,
imprima "Nao existe subsequencia". Mostre o resultado conforme o exemplo de saída."""
c = 1
while True:
    try:
        T = 0
        N1 = input()
        N2 = input()
        lN1 = len(N1)
        for v in range(len(N2)):
            if N1[0:len(N1)] == N2[v:(v+len(N1))]:
                T += 1
                pos = v+1
        if T > 0:
            print(f"Caso #{c}:\n"
                f"Qtd.Subsequencias: {T}\n"
                f"Pos: {pos}\n")
        else:
            print(f"Caso #{c}:\n"
                f"Nao existe subsequencia\n")
        c += 1
    except EOFError:
        break