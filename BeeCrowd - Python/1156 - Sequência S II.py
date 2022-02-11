S = 0
T = 1
for c in range(1, 39, 2):
    S += c/T
    T *= 2
print(f'{S:.2f}')