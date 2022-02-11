"""Robbie é um robô muito carismático, e uma das coisas que ele mais gosta de fazer, além de brincar com Glória, é
colecionar moedas. Robbie possui várias moedas com valores iguais ou diferente, e de mesmo mesmo tamanho. e elas são
guardadas de maneira organizada uma sobre a outra dentro de um cilindro de vidro. Robbie sempre faz um joguinho com
Glória usando suas moedas quando ela pede pra brincar com ele de esconde-esconde, ou quando ela pede pra ele levá-la
para passear. O jogo acontece da seguinte maneira: Glória escolhe um número N que será o salto das moedas que serão
somadas, então a cada Nmoedas o valor Vi da moeda é somado até que não haja mais moedas, ou seja, Σ de
((VM-(N*0))+(VM-(N*1))+(VM-(N*2) )...), M é o número de moedas. Por exemplo, se existirem 5 moedas com os valores
1, 2 , 3, 4 e 5, e Glória escolher 2 como valor do salto, então serão somadas as moedas 5, 3 e 1, resultando em 9,
ao final Robbie verifica se a soma dessas moedas é um número primo, se isso acontecer ele faz o que a Glória quer,
caso contrário, a garotinha convence Robbie a jogar novamente, pois ela sempre consegue convencer ele de tudo, alegando
que deixará de contar histórias pra ele, caso ele não faça a vontade dela.

Você como um bom programador da U.S. Robots, ajudará esses dois amigos, escrevendo um programa irá dizer o resultado do
jogo.

Entrada
A entrada contém vários casos de teste. A primeira linha de um caso de teste contém um inteiro M (2 ≤ M ≤ 20 ) que
representa a quantidade de moedas. Cada uma das próximas M linhas contém um inteiro Vi (1 ≤ Vi ≤ 500) que representa o
valor da moeda Mi , e por último um inteiro N (1 ≤ N ≤ M) que é o salto na soma escolhido por Glória.

A entrada termina em EOF.

Saída
Imprima “You’re a coastal aircraft, Robbie, a large silver aircraft.”, caso Glória ganhe o jogo, ou “Bad boy! I’ll hit
you.”, caso Glória não ganhe o jogo. A saída não deve conter aspas."""


def primo(a):
    if a in (0, 1):
        return f"Bad boy! I’ll hit you."
    for b in range(2, int(a//2)+1):
        if (a % b) == 0:
            return f"Bad boy! I’ll hit you."
    return f"You’re a coastal aircraft, Robbie, a large silver aircraft."


while True:
    try:
        coins = []
        for _ in range(int(input())):
            coins.append(int(input()))
        coins = coins[-1:-len(coins)-1:-int(input())]
        print(primo(sum(coins)))

    except EOFError:
        break
