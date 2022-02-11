X = int(input())
while True:
    Z = int(input())
    if Z <= X:
        continue
    else:
        break

s = 0
M = X
while M <= Z:
    M += X + 1
    s += 1

print(s)


