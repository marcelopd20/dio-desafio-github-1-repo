"""O seu professor de programação gostaria que você fizesse um programa com as seguintes características:

Crie uma variável para armazenar 50 caracteres;
Atribua a variável anterior a frase: "AMO FAZER EXERCICIO NO URI";
Mostre na primeira linha o carácter <, o valor armazenado na variável com o formato "%s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%30s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%.20s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%-20s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%-30s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%.30s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%30.20s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%-30.20s" e o carácter >;
"""
a = 'AMO FAZER EXERCICIO NO URI'
print(f'<{a}>')
print(f'<{a:>30}>')
print(f'<{a[:20]}>')
print(f'<{a:<20}>')
print(f'<{a:<30}>')
print(f'<{a[:30]}>')
print(f'<{a[:20]:>30}>')
print(f'<{a[:20]:<30}>')