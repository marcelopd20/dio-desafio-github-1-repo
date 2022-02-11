tot = c = 0
while True:
    N = int(input())
    if N < 0:
        break
    tot += N
    c += 1
print(f'{tot/c:.2f}')