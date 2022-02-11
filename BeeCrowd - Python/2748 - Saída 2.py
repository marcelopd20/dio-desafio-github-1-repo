"""O seu professor de programação gostaria de fazer uma tela com as seguintes características:

Ter 39 traços (-) na primeira linha;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, embaixo do 10 traço deve começar a
escrever a palavra "Roberto" e o restante preencher no meio com espaço em branco;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, preencher no meio com espaço em branco;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, embaixo do 10 traço deve começar a
escrever o número "5786" e o restante preencher no meio com espaço em branco;
Repita o procedimento 3;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, embaixo do 10 traço deve começar a escrever a palavra "UNIFEI" e o restante preencher no meio com espaço em branco;
Repita o procedimento 1.
No final deve ficar igual a imagem a seguir:

--------------------------------------- (39 traços)
|        Roberto                      |
|                                     |
|        5786                         |
|                                     |
|        UNIFEI                       |
--------------------------------------- (39 traços)
"""
print('-'*39)
print('|', f'{"Roberto":>14}',f'{"|":>22}')
print('|' + f'{"|":>38}')
print('|', f'{"5786":>11}',f'{"|":>25}')
print('|' + f'{"|":>38}')
print('|', f'{"UNIFEI":>13}',f'{"|":>23}')
print('-'*39)