p = n = pa = im = 0

for c in range(5):
    z = int(input())
    if z > 0:
        p += 1
    elif z < 0:
        n += 1
    if z % 2 == 0:
        pa += 1
    else:
        im += 1
print(f'{pa} valor(es) par(es)\n'
    f'{im} valor(es) impar(es)\n'
    f'{p} valor(es) positivo(s)\n'
    f'{n} valor(es) negativo(s)')