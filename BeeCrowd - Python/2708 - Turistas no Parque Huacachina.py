"""A agência de turismo municipal da cidade de Ica, no Peru montou um posto de controle de jipes de aventura que
sobem para as dunas do parque Hucachina. Como durante o dia, são vários os off-roads que sobem e descem do parque
nacional, e nem sempre os turistas usam um mesmo transporte para a ida e volta, a prefeitura precisava ter um melhor
controle e segurança sobre fluxo de visitantes no parque. Desenvolva um programa que receba como entrada se um jipe
está entrando ou voltando do parque e a quantidade de turistas que este veículo está transportando. Ao final do turno,
o programa deve indicar a quantidade de veículos e de turistas que ainda faltam regressar da aventura.

Entrada
O programa deve receber sucessivos pares de entrada. Cada par deve indicar o movimento do jipe e a quantidade de
turistas que este está transportando. A primeira entrada deve ser "SALIDA" ou "VUELTA". "SALIDA" deve indicar que o
jipe está saindo da central e entrando no parque; e "VUELTA" que o jipe está retornando do passeio. Imediatamente na
 sequência, o programa recebe um número inteiro T (onde, 0 <= T <=20) que indica a quantidade de turistas que estão
 sendo transportados pelo jipe. A string "ABEND" deve ser o indicador de fim de processamento.

Saída
Como objetivo o programa deve apresentar duas saídas, uma em cada linha: a quantidade de turistas e a quantidade de
jipes que ainda faltam voltar do parque."""
t = j = 0
while True:
    A = input()
    if A == "ABEND":
        break
    else:
        A, T = A.split()
        if A in 'SALIDA':
            j += 1
            t += int(T)
        elif A in 'VUELTA':
            j -= 1
            t -= int(T)
print(f'{t}\n{j}')
