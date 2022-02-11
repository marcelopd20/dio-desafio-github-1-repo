N = int(input())
for b in range(0, N):
    sd = 0
    X = int(input())
    for c in range(1, X):
        if X % c == 0:
            sd += c
    print(f'{X} eh perfeito') if X == sd else print(f'{X} nao eh perfeito')
