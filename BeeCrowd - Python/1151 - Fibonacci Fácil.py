F1 = 0
F2 = 1
N = int(input())
for c in range(0, N if N < 47 else 0):
    print(f"{F1}", end=' ') if c < N-1 else print(f'{F1}')
    F3 = F1 + F2
    F1 = F2
    F2 = F3
