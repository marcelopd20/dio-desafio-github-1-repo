a = []
b = []
while True:
    s = 0
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    a.append(m)
    b.append(n)
for i, v in enumerate(a):
    if a[i] < b[i]:
        for c in range(a[i], b[i]+1):
            print(c, end=' ')
            s += c
    else:
        for c in range(b[i], a[i]+1):
            print(c, end=' ')
            s += c
    print(f'Sum={s}')
    s = 0
