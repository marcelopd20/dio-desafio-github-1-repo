N = int(input())
for c in range(1, (N*4)+1):
    if c % 4 != 0:
        print(f'{c} ', end='')
    else:
        print('PUM')