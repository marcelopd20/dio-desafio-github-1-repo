"""Chegamos finalmente no final do semestre e pra variar, trabalhos estão acumulados! Os professores, com a
intenção de ajudar (ou não), decidiram que os trabalhos será feitos em duplas, além disso, eles dariam o spoiler do
grau de dificuldade que um trabalho tem para ser feito.

Sabendo disso, Rangel, nosso velho amigo, escolheu Gugu como sua dupla, pois ele sabe que Gugu é um cara responsável.
Como ambos estão apertados eles decidiram dividir os trabalhos com os seguintes critérios:

A ordem dos trabalhos não pode ser alterada durante a divisão;

A divisão precisa ser justa, ou seja, minimizar a diferença entre os trabalhos feitos por Rangel e por Gugu;

Rangel sempre faz os primeiros e trabalhos e Gugu o restante.

Como os dois estão muito ocupados na biblioteca pegando os livros para resolverem os trabalhos, eles pediram a você para
 determinar a diferença.

Entrada
O arquivo contém vários casos de teste. A primeira linha de cada caso contém um inteiro N (1 ≤ N ≤ 106) que indica o
número de elementos da sequência, na segunda linha contém N inteiros onde cada inteiro possui um valor X (1 ≤ X ≤105).

A entrada termina com um EOF.

Saída
Para cada caso de teste, um inteiro Y deve ser impresso, onde Y é o valor da diferença ótima seguindo os critérios do
problema. Deixe uma linha em branco após cada caso de teste, inclusive após o último."""

while True:
    try:
        N = int(input())
        X = [int(x) for x in input().split()]
        c = 0
        a = X[0]
        b = sum(X[1:])
        while a < b:
            c += 1
            a += X[c]
            if a < b:
                b -= X[c]
            else:
                a -= X[c]
                break
        print(abs(b- a))
        print()
    except EOFError:
        break
