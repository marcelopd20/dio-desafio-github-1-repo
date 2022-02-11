s = c = r = 0
n = int(input())
for x in range(n):
    qnt, sp = input().split()
    if sp in 'Cc':
        c += int(qnt)
    elif sp in 'Rr':
        r += int(qnt)
    elif sp in 'Ss':
        s += int(qnt)
animais = {'coelhos': c, 'ratos': r, 'sapo': s, 'total': c+r+s}
print(f'Total: {animais["total"]} cobaias\n'
      f'Total de coelhos: {animais["coelhos"]}\n'
      f'Total de ratos: {animais["ratos"]}\n'
      f'Total de sapos: {animais["sapo"]}\n'
      f'Percentual de coelhos: {(animais["coelhos"]*100)/animais["total"]:.2f} %\n'
      f'Percentual de ratos: {(animais["ratos"]*100)/animais["total"]:.2f} %\n'
      f'Percentual de sapos: {(animais["sapo"]*100)/animais["total"]:.2f} %')
