a = []
n = int(input())
for c in range(n):
    x1, x2, x3 = map(float, input().split())
    m = ((x1*2) + (x2*3) + (x3*5))/10
    a.append(m)
for i,v in enumerate(a):
    print(f'{v:.1f}')