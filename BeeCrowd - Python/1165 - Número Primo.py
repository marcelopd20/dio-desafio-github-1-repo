N = int(input())
for c in range(0, N):
    X = int(input())
    n = 0
    for b in range(1, X):
        if X % b == 0:
            n += 1
    print(f'{X} eh primo') if n == 1 or X == 1 else print(f'{X} nao eh primo')
