"""Júlio está criando um novo Smart Watch especialmente para programadores. É impressionante as vantagens que ele
oferece e o conforto pra codar que ele tem. O relógio ainda está em desenvolvimento e ele prometeu consertar os bugs e
colocar uns apetrechos melhores e, em troca, pediu um sistema simples para o modo Standy Bay. O problema é que o
relógio por si só sempre tem o ângulo de inclinação do Sol/Lua(de 0 a 360). Valendo um relógio, caso deseja aceitar:
dada em grau da inclinação do Sol/Lua, informe em qual período do dia ele se encontra.

Entrada
A entrada contém um número inteiro M (0 ≤ M ≤ 360) representando o grau do Sol/Lua. Como a posição muda constantemente
seu programa receberá diversos casos a cada segundo(EOF).

Saída
Imprima uma saudação referente ao período do dia que ele se encontra: "Boa Tarde!!", "Boa Noite!!", "Bom Dia!!" e "De
Madrugada!!"."""
def busca(a):
    dici = {'Bom Dia!!': list(range(0, 90)), 'Boa Tarde!!': list(range(90, 180)),
            'Boa Noite!!': list(range(180, 270)), 'De Madrugada!!': list(range(270, 360))}
    for k, v in dici.items():
        if a == 360:
            return 'Bom Dia!!'
        elif a in v:
            return k

while True:
    try:
        print(busca(int(input())))

    except EOFError:
        break
