a = []
n = int(input())
for c in range(n):
    x = int(input())
    a.append(x)
for i, v in enumerate(a):
    if v == 0:
        print('NULL',)
    elif v % 2 == 0:
        print('EVEN', end=' ')
    else:
        print('ODD', end=' ')
    if v > 0:
        print('POSITIVE')
    elif v < 0:
        print('NEGATIVE')
