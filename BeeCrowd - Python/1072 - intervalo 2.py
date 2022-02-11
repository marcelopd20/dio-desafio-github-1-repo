a = list()
n = int(input())
xin = xout = 0
for c in range(n):
    x = int(input())
    a.append(x)
for i, v in enumerate(a):
    if 10 <= v <= 20:
        xin += 1
    else:
        xout += 1
print(f'{xin} in\n{xout} out')
