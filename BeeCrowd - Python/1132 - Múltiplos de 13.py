x = int(input())
y = int(input())
s = 0

for c in (range(x, y+1) if x < y else range(y, x+1)):
    if c % 13 != 0:
        s += c
print(s)
