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


nota1 = leiaNota('')
nota2 = leiaNota('')
media = (nota1+nota2)/2
print(f'media = {media:.2f}')
