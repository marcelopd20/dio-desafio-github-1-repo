N = int(input())
X = list()
a = list(map(int, input().split()))
for c in range(N):
    X.append(a[c])
print(f'Menor valor: {min(X)}')
print(f'Posição: {X.index(min(X))}')
