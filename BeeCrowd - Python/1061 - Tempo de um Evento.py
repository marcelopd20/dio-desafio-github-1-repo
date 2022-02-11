d1s = input('').replace("Dia ", "").split()
d1 = int(d1s[0])
h1, m1, s1 = map(int, input().replace(':', "").split())
d2s = input('').replace("Dia ", "").split()
d2 = int(d2s[0])
h2, m2, s2 = map(int, input().replace(':', "").split())
ts1 = (d1 * 86400) + (h1 * 3600) + (m1 * 60) + s1
ts2 = (d2 * 86400) + (h2 * 3600) + (m2 * 60) + s2
tse = ts2 - ts1
de = tse // 86400
tse %= 86400
he = tse // 3600
tse %= 3600
me = tse // 60
se = tse % 60
print(f'{de} dia(s)\n{he} hora(s)\n{me} minuto(s)\n{se} segundo(s)')
