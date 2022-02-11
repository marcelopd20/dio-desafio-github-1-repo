n = float(input())
if 0 <= n <= 25:
    print(f'Intervalo (0,25)')
elif 25 < n <= 50:
    print(f'Intervalo (25,50)')
elif 50 < n <= 75:
    print(f'Intervalo (50,75')
elif 75 < n <= 100:
    print(f'Intervalo (75,100)')
else:
    print('Fora de intervalo')
