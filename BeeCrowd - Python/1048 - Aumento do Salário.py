sal = float(input())
if sal <= 400:
    r = sal * 0.15
    p = '15 %'
elif 400 < sal <= 800:
    r = sal * 0.12
    p = '12 %'
elif 800 < sal <= 1200:
    r = sal * 0.1
    p = '10 %'
elif 1200 < sal <= 2000:
    r = sal * 0.07
    p = '7 %'
else:
    r = sal * 0.04
    p = '4 %'
ns = sal + r
print(f'Novo salario: {ns:.2f}\n'
      f'Reajuste ganho: {r:.2f}\n'
      f'Em percentual: {p}')
