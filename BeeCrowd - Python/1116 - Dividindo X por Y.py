a = []
n = int(input())
di = 'divisao impossivel'
for c in range(n):
    x, y = map(int, input().split())
    if y == 0:
        a.append(di)
    else:
        a.append(x / y)
    for i, v in enumerate(a):
        print(v)
