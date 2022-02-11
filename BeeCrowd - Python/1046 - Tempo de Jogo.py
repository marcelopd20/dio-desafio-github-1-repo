a, b = map(int, input().split())
if a < b:
    t = b - a
else:
    t = b + 24 - a
print(f'O JOGO DUROU {t} HORA(S)')
