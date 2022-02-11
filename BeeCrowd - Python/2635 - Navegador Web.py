"""Lucas é um rapaz bem radical quando o assunto envolve licenças de software. Desde que começou sua graduação em
engenharia da computação, ele procura desenvolver todas as ferramentas que necessita. Tudo isso começou após
experiências ruins ao utilizar softwares proprietários. Agora, ele acredita que um programador de verdade deve ser
autossuficiente, ou seja, deve construir todos os programas que precisa, desde uma simples calculadora até seu próprio
sistema operacional.

Este semestre, Lucas está cursando a disciplina de desenvolvimento de sistemas web. Para continuar sua filosofia de
vida, utilizando apenas softwares construı́dos por ele mesmo, Lucas já está programando seu próprio web browser. Grande
parte do trabalho foi concluı́da, porém algumas funcionalidades ainda precisam ser finalizadas.

O navegador de Lucas possui um campo de busca onde o usuário poderá inserir uma palavra chave, e ao clicar em um botão
de confirmação, ele será redirecionado para outra página com os resultados de sua pesquisa. Quando alguma string for
digitada no campo de busca, Lucas quer que seu programa exiba, logo abaixo, algumas opções para auto completar esta
string de acordo com as buscas já realizadas pelo usuário.

Por exemplo, se as palavras “algoritmos” e “algas” já foram pesquisadas, ao digitar a string “alg”, o programa deverá
sugerir as palavras “algoritmos” e “algas”. Portanto, para cada string digitada, o programa deverá sugerir palavras
pesquisadas anteriormente e que possuem como prefixo esta string. Caso alguma palavra seja igual a string digitada,
ela também deve ser sugerida.

Lucas está preocupado com a quantidade de palavras que seu programa pode sugerir, além do tamanho máximo que elas podem
alcançar. Por isso, ele pediu que você o ajude escrevendo um programa em que dadas algumas palavras já pesquisadas e uma
 série de consultas compostas por uma string, indique quantas palavras o navegador deverá sugerir ao usuário, além do
 comprimento da maior dessas palavras.

Entrada
A entrada é composta por vários casos de teste. A primeira linha de um caso de teste possui um inteiro N (1 ≤ N ≤ 104 )
indicando o número de palavras que já foram pesquisadas pelo programa de Lucas. Cada uma das próximas N linhas contém
uma string não vazia de no máximo 100 letras minúsculas [a − z]. Para cada caso de teste, as N palavras são diferentes.
Em seguida, haverá um inteiro Q (1 ≤ Q ≤ 100) indicando o número de consultas. Cada uma das próximas Q linhas descreve
uma consulta com uma string não vazia de no máximo 100 letras minúsculas [a − z], representando uma string digitada no
campo de busca.

Saída
Para cada caso de teste imprima Q linhas, onde a i-ésima linha é a resposta para a i-ésima consulta. A resposta de cada
consulta deverá ser composta por dois inteiros separados por espaço, representando, respectivamente, o número de
palavradas sugeridas pelo programa ao digitar a string indicada pela i-ésima consulta, e o comprimento da maior palavra
contida nesse subconjunto. Caso nenhuma palavra seja sugerida, imprima -1. Imprima uma linha em branco ao final de cada
caso de teste."""


def search(a):
    la = []
    for l in ls:
        if l.startswith(a):
            la.append(l)
    return [print(f'{len(la)} {len(max(la, key=len))}') if bool(la) else print(-1)]


ls = list()
for c in range(int(input())):
    ls.append(input())
for c in range(int(input())):
    search(input())
