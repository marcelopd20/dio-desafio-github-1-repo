def leiaC(cont):
    while True:
        try:
            c = int(input(cont))
            if c not in (1, 2):
                continue
            else:
                return c
        except:
            continue


gr = emp = ig = gg = 0
cont = 1
while cont == 1:
    i, g = map(int, input().split())
    gr += 1
    if i == g:
        emp += 1
    elif i > g:
        ig += 1
    else:
        gg += 1
    cont = leiaC('Novo grenal (1-sim 2-nao)\n')
print(f'''{gr} grenais
Inter:{ig}
Gremio:{gg}
Empates:{emp}''')
if ig > gg:
    print('Inter venceu mais')
elif gg > ig:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')

