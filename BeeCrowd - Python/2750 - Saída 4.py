"""O seu professor de programação gostaria que você fizesse um programa com as seguintes características:

Criar 16 variáveis inteiras;
Atribuir a elas valores de 0 a 15 a cada um das variáveis anteriores;
Ter 39 traços (-) na primeira linha;
Ter uma | embaixo do primeiro traço, décimo terceiro, vigésimo terceiro e do trigésimo nono traço da primeira linha,
embaixo do 4o traço deve começar a escrever “decimal”, embaixo do 16o traço deve começar a escrever “octal”, embaixo do
26o traço deve começar a escrever “Hexadecimal” e o restante preencher com espaço em branco;
Repita o procedimento 1;
Ter uma | embaixo do primeiro traço, décimo terceiro, vigésimo terceiro e do trigésimo nono traço da primeira linha,
embaixo do 8o traço deve imprimir o valor da primeira variável em valor decimal, embaixo do 18o traço deve imprimir o
valor da primeira variável em valor octal, embaixo do 31o traço deve imprimir o valor da primeira variável em valor
hexadecimal e o restante preencher com espaço em branco;
Repita o procedimento 6 para as outras 15 variáveis;
Repita o procedimento 1.
No final deve ficar igual a imagem a seguir:

--------------------------------------- (39 traços)
| decimal   |  octal  |  Hexadecimal  |
---------------------------------------
|      0    |    0    |       0       |
|      1    |    1    |       1       |
|      2    |    2    |       2       |
|      3    |    3    |       3       |
|      4    |    4    |       4       |
|      5    |    5    |       5       |
|      6    |    6    |       6       |
|      7    |    7    |       7       |
|      8    |   10    |       8       |
|      9    |   11    |       9       |
|     10    |   12    |       A       |
|     11    |   13    |       B       |
|     12    |   14    |       C       |
|     13    |   15    |       D       |
|     14    |   16    |       E       |
|     15    |   17    |       F       |
--------------------------------------- (39 traços)"""

print('-'*39)
print('|', f"{'decimal':>8}", f"{'|':>2}", f"{'octal':>6}", f"{'|':>2}", f"{'Hexadecimal':>12}",f"{'|':>2}")
print('-'*39)
for x in range(16):
    print(f'|', f'{x:>6}',f'{"|":>4}',f'{x:>4o}', f'{"|":>4}', f'{x:>7X}',f'{"|":>7}')
print('-'*39)