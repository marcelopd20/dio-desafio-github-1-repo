x = map(int, input().split())
a, b = sorted(list(x))
if b % a == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
    