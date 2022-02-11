X, Y = map(int, input().split())
[print(f'{c} ', end='') if c % X != 0 else print(f'{c}') for c in range(1, Y+1)]
