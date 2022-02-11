a = []
n = int(input())
s = 0
for c in range(n):
    x, y = map(int, input().split())
    if x < y:
        for b in range(x+1, y):
            if b % 2 != 0:
                s += b
        a.append(s)
    else:
        for b in range(y+1, x):
            if b % 2 != 0:
                s += b
        a.append(s)
    s = 0
for i, v in enumerate(a):
    print(v)
