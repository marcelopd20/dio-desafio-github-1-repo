"""Ultimamente, diversas pessoas estão indo à Dra. Cláudia Café com Leite para saber se estão consumindo a
quantidade recomendada diária de vitamina C. Isso tem a deixado exausta, e por isso ela lhe pediu para escrever um
programa que, dado o consumo diário de alimentos ricos em vitamina C por uma pessoa, indique o quanto essa pessoa deve
consumir a mais ou a menos para atingir o recomendado.

Para tal, você poderá utilizar a tabela a seguir:

Alimentos ricos em Vitamina C	Quantidade de Vitamina C
suco de laranja	120 mg
morango fresco	85 mg
mamao	85 mg
goiaba vermelha	70 mg
manga	56 mg
laranja	50 mg
brocolis	34 mg
Considere que o consumo diário recomendado de vitamina C está entre 110 mg e 130 mg, inclusive.

Entrada
Cada caso de teste é composto um inteiro T (1 ≤ T ≤ 7) indicando que a pessoa consome diariamente T alimentos entre os
7 alimentos da tabela. Em seguida, haverá T linhas com um inteiro N e um alimento (totalmente em caixa baixa e sem
acentuações), indicando que a pessoa consome uma quantidade N daquele alimento. A entrada termina com T = 0.

Saída
Para cada caso de teste (T), se o consumo ultrapassou o limite recomendado, imprima "Menos X mg", em que X representa a
quantidade a menos a ser consumida para atingir o limite recomendado; se o consumo não atingiu o recomendado, imprima
"Mais X mg", em que X representa a quantidade a mais para atingir o recomendado; se o consumo está dentro do intervalo
recomendado, imprima "X mg", em que X representa a quantidade consumida diariamente pela pessoa."""
sl = 120
mf = m = 85
g = 70
ma = 56
l = 50
b = 34
while True:
    T = int(input())
    if T == 0:
        break
    tot = 0
    for c in range(T):
        L = str(input())
        Q = int(L[0:L.index(' ')])
        L = L[2:len(L)]
        tot += Q * (sl if 'suco de laranja' in L else mf if 'morango' in L else m if 'mamao' in L else g if 'goiaba' in L else ma if 'manga' in L else l if 'laranja' in L else b if 'brocolis' in L else 0)
    if tot > 130:
        print(f'Menos {tot - 130} mg')
    elif tot < 110:
        print(f'Mais {110 - tot} mg')
    else:
        print(tot, 'mg')
