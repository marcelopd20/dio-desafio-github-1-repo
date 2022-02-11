def leiaCod(msg):
    while True:
        try:
            cod = int(input(msg))
            if cod not in range(1, 5):
                continue
            else:
                return cod
        except:
            continue


dici = dict()
c = 1
a = g = d = 0
while c != 4:
    c = leiaCod('')
    if c == 1:
        a += 1
    elif c == 2:
       g += 1
    elif c == 3:
        d += 1
print(f'''MUITO OBRIGADO
Alcool: {a}
Gasolina: {g}
Diesel: {d}''')
