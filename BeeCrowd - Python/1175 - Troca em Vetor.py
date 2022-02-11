N = list()
for c in range(0, 20):
    X = int(input())
    N.append(X)
N.reverse()
for i, v in enumerate(N):
    print(f'N[{i}] = {v}')