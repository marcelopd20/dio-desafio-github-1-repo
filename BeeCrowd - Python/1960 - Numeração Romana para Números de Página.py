"""A ECI (Editio Chronica Incredibilis ou Editora de Crônicas Incríveis) é muito tradicional quando se trata
de numerar as páginas de seus livros. Ela sempre usa a numeração romana para isso. E seus livros nunca ultrapassam
as 999 páginas pois, quando necessário, dividem o livro em volumes.

Você deve escrever um programa que, dado um número arábico, mostra seu equivalente na numeração romana.

Lembre que I representa 1, V é 5, X é 10, L é 50, C é 100, D é 500 e M representa 1000.

Entrada
A entrada é um número inteiro positivo N (0 < N < 1000).

Saída
A saída é o número N escrito na numeração romana em uma única linha. Use sempre letras maiúsculas."""
N = int(input())
M = N // 1000
N = N % 1000
F = str()
if M == 1:
    F += 'M'
M = N // 100
N = N % 100
if M == 9:
    F += 'CM'
elif M >= 5:
    F += 'D'
    for c in range(5,M):
        F += 'C'
elif M == 4:
    F += 'CD'
elif M < 4:
    for c in range(M):
        F += 'C'
M = N // 10
N = N % 10
if M == 9:
    F += 'XC'
elif M >= 5:
    F += 'L'
    for c in range(5,M):
        F += 'X'
elif M == 4:
    F += 'XL'
elif M < 4:
    for c in range(M):
        F += 'X'
if N == 9:
    F += 'IX'
elif N >= 5:
    F += 'V'
    for c in range(5,N):
        F += 'I'
elif N == 4:
    F += 'IV'
elif N < 4:
    for c in range(N):
        F += 'I'
print(F)

