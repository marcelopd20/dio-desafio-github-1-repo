"""Samu Elmito adora criar jogos peculiares para desafiar seus amigos. Desta vez, ele inventou um jogo chamado
"Jogo do Operador", em que ele cria expressões básicas e cada jogador deve escolher uma expressão e preencher a
lacuna com o operador correto para validá-la. Os jogadores poderão escolher operadores de somente três tipos:
adição, subtração e multiplicação. Porém, se o jogador achar que não há operador entre os três tipos que valide a
expressão, poderá responder Impossível.

Sua tarefa é simples: dadas as expressões e as respostas dos jogadores, determinar os jogadores que não passarão para a
outra fase do jogo.

Entrada
A entrada é composta por um inteiro T (2 ≤ T ≤ 50) que indica a quantidade de expressões e de jogadores. Cada caso de
teste é composto por T expressões na forma "X Y=Z", indicando que X operador Y (0 ≤ X, Y ≤ 103) é igual a Z
(-103 ≤ Z ≤ 106), seguido de T jogadores e suas respectivas respostas na forma "N E R", sendo N o nome do jogador
(até 50 caracteres e sem espaços), E o índice da expressão escolhida (1 ≤ E ≤ T) e R a resposta (+, -, * ou I,
indicando Impossível). A entrada termina com EOF (fim de arquivo).

Saída
Para cada caso de teste, se todos os jogadores passarem, imprima "You Shall All Pass!"; se nenhum jogador passar,
imprima "None Shall Pass!"; caso contrário, imprima, em ordem lexicográfica e entre espaços, o nome dos jogadores
que erraram a resposta e, desta forma, não passarão para a próxima fase do jogo."""
while True:
    try:
        cts = list()
        np = list()
        T = int(input())
        for c in range(T):
            L = input()
            p = int(L[0:L.index(' ')])
            s = int(L[L.index(' '):L.index('=')])
            t = int(L[L.index('=')+1:len(L)])
            cts.append([p, s, t])
        for l in range(T):
            n, e, r = input().split()
            e = int(e)-1
            if r == '+':
                if cts[e][0] + cts[e][1] == cts[e][2]:
                    F = True
                else:
                    F = False
            elif r == '-':
                if cts[e][0] - cts[e][1] == cts[e][2]:
                    F = True
                else:
                    F = False
            elif r == '*':
                if cts[e][0] * cts[e][1] == cts[e][2]:
                    F = True
                else:
                    F = False
            elif r == 'I':
                if cts[e][0] * cts[e][1] != cts[e][2] and cts[e][0] + cts[e][1] != cts[e][2] and cts[e][0] - cts[e][1] \
                        != cts[e][2]:
                    F = True
                else:
                    F = False
            if F == False:
                np.append(n)

        if len(np) == 0:
            print('You Shall All Pass!')
        elif len(np) < T:
            np.sort()
            for i, v in enumerate(np):
                [print(v, end=' ') if i < len(np)-1 else print(v)]
        else:
            print('None Shall Pass!')
    except EOFError:
        break