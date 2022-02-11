def leiaNota(nota):
    while True:
        try:
            n = float(input(nota))
            if n < 0 or n > 10:
                print('nota invalida')
                continue
            else:
                return n
        except:
            continue

def leiaCont(c):
    while True:
        try:
            co = int(input(c))
            if co not in (1, 2):
                continue
            else:
                return co
        except:
            continue
i = 1
while i == 1:
    nota1 = leiaNota('')
    nota2 = leiaNota('')
    media = (nota1+nota2)/2
    print(f'media = {media:.2f}')
    i = leiaCont('novo calculo (1-sim 2-nao)\n')
