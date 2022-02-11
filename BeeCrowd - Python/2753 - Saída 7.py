"""O seu professor de programação gostaria que você fizesse um programa com as seguintes características:

Crie vinte e seis variáveis inteira;
Atribua a primeira variável o valor 97;
Atribua as outras demais variável o valor da primeira somado de uma unidade;
Mostre na tela os valores numéricos da primeira variável, um espaço em braco, o carácter 'e', outro espaço em branco e o seu valor alfanumérico (caracteres);
Repita o procedimento para todas as outras variáveis."""

for x in range(97, 123):
    print(f'{x} e {chr(x)}')