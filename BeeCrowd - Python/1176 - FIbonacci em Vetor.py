T = int(input())
T1 = 0
T2 = 1
fib = list()
for c in range(0, 61):
    fib.append(T1)
    T3 = T1 + T2
    T1 = T2
    T2 = T3
for c in range(0, T):
    N = int(input())
    print(f'Fib({N}) = {fib[N]}')
