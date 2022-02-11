"""No tower defense Magic and Sword, o jogador pode lançar magias de área para derrotar as unidades inimigas. As
magias são elementais: fogo, água, ar e terra, e a região afetada é determinada por um círculo cujo raio depende do
nível da magia.

A tabela abaixo lista cada magia, o dano e o respectivo raio por nível:



As unidades inimigas são delimitadas por um retângulo de largura w e altura h, com canto inferior esquerdo posicionado
no ponto (x0, y0). O inimigo sofrerá dano caso seu retângulo delimitador tenha qualquer intercessão com a área deﬁnida
pelo círculo da magia.

Dada a posição e o retângulo delimitador da unidade inimiga, o centro da explosão e o identiﬁcador e o nível da magia,
determine o dano sofrido pela unidade. Caso a unidade esteja fora do alcance da magia, o dano sofrido é igual a zero.

Entrada
A entrada consiste em T (1 ≤ T ≤ 1000) casos de teste, onde o valor de T é informado na primeira linha da entrada.
Cada caso de teste é composto por duas linhas. A primeira contém quatro número inteiros que repre-sentam as dimensões
w e h (1 ≤ w, h ≤ 1000) do retângulo e as coordenadas x0 e y0 (0 ≤ x0, y0 ≤ 1000) do canto inferior esquerdo. A segunda
linha do caso de teste contém uma string com o identiﬁcador da magia (ﬁre para fogo, water para água, earth para terra
e air para ar), o nível N desta magia (1 ≤ N ≤ 3) e as coordenadas cx e cy (0 ≤ cx, cy ≤ 1000) do centro da área da
explosão.

Saída
Para cada caso de teste, a saída deve ser o valor do dano recebido pela unidade, seguido de uma quebra de linha."""
from dataclasses import dataclass
from typing import Dict


@dataclass
class Mag:
    dn: int
    lvl: Dict[int, int]


fire = Mag(200, {1: 20, 2: 30, 3: 50})
water = Mag(300, {1: 10, 2: 25, 3: 40})
earth = Mag(400, {1: 25, 2: 55, 3: 70})
air = Mag(100, {1: 18, 2: 38, 3: 60})


def atk():
    dici = {'fire': fire, 'water': water, 'earth': earth, 'air': air}
    w, h, x0, y0 = (int(x) for x in input().split())
    inp = input().split()
    n, cx, cy = [int(x) for x in inp[1:]]
    inp = inp[0]
    x_ponto = cx
    y_ponto = cy
    if cx < x0:
        x_ponto = x0
    elif cx > x0 + w:
        x_ponto = x0 + w

    if cy < y0:
        y_ponto = y0
    elif cy > y0 + h:
        y_ponto = y0+h

    dist_x = cx - x_ponto
    dist_y = cy - y_ponto
    dist = ((dist_x**2 + dist_y**2)**(1/2))

    if dist <= dici[inp].lvl[n]:
        return dici[inp].dn
    return 0

op = []

for _ in range(int(input())):
    op.append(atk())
print(*op, sep='\n')

