"""Novamente Júlio pede sua ajuda, ele esqueceu de um pequeno detalhe.
Como o seu o programa anterior só informava uma
saudação, ele pediu que transformasse o grau do Sol/Lua em HH:MM:SS.
Então caso aceite: dado um grau relativo a posição do Sol/Lua, refaça o sistema só que agora além da saudação de cada
período do dia, informe exatamente as horas, os minutos e segundos.

Entrada
A entrada contem um pontos flutuantes M (0 ≥ M < 360) representando a posição, em graus,do Sol/Lua em relação a terra.
Como eles andam em constante movimento seu programa receberá diversos casos a cada segundo(EOF).

Saída
Imprima qual período do dia ele se encontra: "Boa Tarde!!", "Boa Noite!!", "Bom Dia!!" e "De Madrugada!!", e na linhas
de baixo exiba as horas, minutos e segundos (HH:MM:SS)."""


def busca(a):
    b = hora(a)
    a = int(a)
    dici = {'Bom Dia!!': list(range(0, 90)), 'Boa Tarde!!': list(range(90, 180)),
            'Boa Noite!!': list(range(180, 270)), 'De Madrugada!!': list(range(270, 360))}
    for k, v in dici.items():
        if a == 360:
            return 'Bom Dia!!\n06:00:00'
        elif a in v:
            return f'{k}\n{b}'

def hora(a):
    s = int((a * 240) % 60)
    m = int((a * 240) % 3600)//60
    h = int(((a * 240) // 3600) + 6)
    if h >= 24:
        h -= 24
    return f'{h if h >= 10 else f"0{h}"}:{m if m >= 10 else f"0{m}"}:{s if s >= 10 else f"0{s}"}'
while True:
    try:
        print(busca(float(input())))

    except EOFError:
        break
