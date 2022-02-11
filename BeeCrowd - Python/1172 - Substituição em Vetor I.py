X = list()
for c in range(0, 10):
    L = int(input())
    if L <= 0:
        L = 1
    X.append(L)
for v, i in enumerate(X):
    print(f'X[{v}] = {i}')