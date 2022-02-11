def leiaN(a):
    while True:
        try:
            N = int(input(a))
            if N > 50:
                continue
            else:
                return N
        except:
            continue


N = list()
V = leiaN('')
for c in range(0, 10):
    N.append(V)
    V *= 2
for i, v in enumerate(N):
    print(f'N[{i}] = {v}')
