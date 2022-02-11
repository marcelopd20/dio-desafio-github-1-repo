sfilo = input()
clas = input()
ord = input()
if sfilo == 'vertebrado':
    if clas == 'ave':
        if ord == 'carnivoro':
            print('aguia')
        elif ord == 'onivoro':
            print('pomba')
    elif clas == 'mamifero':
        if ord == 'onivoro':
            print('homem')
        elif ord == 'herbivoro':
            print('vaca')
if sfilo == 'invertebrado':
    if clas == 'inseto':
        if ord == 'hematofago':
            print('pulga')
        elif ord == 'herbivoro':
            print('lagarta')
    elif clas == 'anelideo':
        if ord == 'hematofago':
            print('sanguessuga')
        elif ord == 'onivoro':
            print('minhoca')
