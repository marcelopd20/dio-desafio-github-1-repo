"""O seu professor de programação gostaria de fazer uma tela com as seguintes características:

Ter 39 traços (-) na primeira linha;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, embaixo do 2o traço deve começar a
escrever "x = 35" e o restante preencher com espaço em branco;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, preencher no meio com espaço em branco;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, embaixo do 17o traço deve começar a
escrever "x = 35" e o restante preencher com espaço em branco;
Repita o procedimento 3;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, embaixo do 33o traço deve começar a
escrever "x = 35" e o restante preencher no meio com espaço em branco;
Repita o procedimento 1.
No final deve ficar igual a imagem a seguir:

--------------------------------------- (39 traços)

|x = 35                               |

|                                     |

|                x = 35               |

|                                     |

|                               x = 35|

--------------------------------------- (39 traços)"""
print('-'*39)
print('|'+'x = 35'+ f'{"|":>32}')
print('|', f"{'|':>37}")
print(f'{"|"}{"x = 35":^36}{"|":>2}')
print('|', f"{'|':>37}")
print("|", f"{'x = 35|':>37}")
print('-'*39)