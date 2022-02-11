sal = float(input())
while True:
    if sal > 2000:
        nsal = (sal - 2000)
        if nsal > 1000:
            nsal = 1000
        ir = nsal * 0.08
        if sal > 3000:
            nsal1 = (sal - 3000)
            if nsal1 > 1500:
                nsal1 = 1500
            ir1 = nsal1 * 0.18
            ir += ir1
            if sal > 4500:
                ir2 = (sal - 4500) * 0.28
                ir += ir2
    else:
        print('Isento')
        break
    print(f'R$ {ir:.2f}')
    break
