"""Depois de capturar muitos Pomekons, Dabriel e Guarte resolveram batalhar. A forma de duelo é simples,
cada treinador coloca um Pomekon na batalha e vence quem tem o Pomekon com maior valor de golpe, que é definido
da seguinte maneira:

O Bônus será dado ao Pomekon do treinador que estiver em um level de valor par.

Neste problema será dado a você o valor do bônus aplicado, os valores de ataque e defesa do Pomekon de Dabriel e
Guarte e seus respectivos níveis, cabe a você informar o ganhador da batalha.

Entrada
A entrada é composta por diversas instâncias. A primeira linha da entrada contém um inteiro T indicando o número de
instâncias. Cada instância começa com um inteiro B (0 ≤ B ≤ 100), que indica o valor do bônus aplicado. Nas
duas linhas seguintes terão três inteiros Ai, Di e Li (1 ≤ Ai, Di ≤ 100, 1 ≤ Li ≤ 50), representado o valor de
ataque do Pomekon, o valor de defesa e o level do treinador. A primeira linha representa o Pomekon de Dabriel e
a segunda o de Guarte.

Saída
Para instância na entrada você deverá imprimir o nome do treinador que irá vencer a batalha, em caso de empate imprima: "Empate", sem aspas."""
for T in range(int(input())):
    B = int(input())
    D = list()
    for c in range(2):
        Ai, Di, Li = (int(x) for x in input().split())
        if Li % 2 == 0:
            Vgi = ((Ai+Di)/2) + B
        else:
            Vgi = ((Ai + Di) / 2)
        D.append(Vgi)
    if D[0] > D[1]:
        print('Dabriel')
    elif D[0] < D[1]:
        print('Guarte')
    else:
        print('Empate')
