N = int(input())
for c in range(N-1 if N < 13 else 0, 0, -1):
    N *= c
print(N)