x = int(input())
y = int(input())

for c in (range(x+1, y) if x < y else range(y+1, x)):
    if c % 5 == 2 or c % 5 == 3:
        print(c)
