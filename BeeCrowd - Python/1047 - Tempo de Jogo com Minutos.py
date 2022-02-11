hi, mi, hf, mf = map(int, input().split())
h = m = 0
if hi > hf:
    h = hf + 24 - hi
    if mi > mf:
        m = mf + 60 - mi
        h -= 1
    else:
        m = mf - mi
else:
    h = hf - hi
    if mi > mf:
        m = mf + 60 - mi
        h -= 1
    else:
        m = mf - mi
if hi == hf:
    h = 24
    if mi == mf:
        h = 24
    elif mi > mf:
        h -= 1
    elif mf > mi:
        h = 0
if m >= 60:
    h += 1
    m = m - 60
print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')
