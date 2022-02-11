lista = list(map(int, input().split()))
n = 1
s = 0

while lista[n] <= 0:
    if lista[n] <= 0:
        n += 1
    elif lista[n] > 0:
        break

for c in range(0,lista[n]):
    s += lista[0] + c

print(s)