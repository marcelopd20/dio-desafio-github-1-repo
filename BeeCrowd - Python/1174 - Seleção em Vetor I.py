a = list()
for c in range(0,100):
    N = float(input())
    a.append(N)
for i, v in enumerate(a):
    if v <= 10:
        print(f'A[{i}] = {v:.1f}')