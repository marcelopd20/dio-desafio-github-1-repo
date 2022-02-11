b = s = 0
for c in range(6):
    p = float(input())
    if p > 0:
        b += 1
        s += p
print(f'{b} valores positivos\n'
      f'{s/b:.1f}')