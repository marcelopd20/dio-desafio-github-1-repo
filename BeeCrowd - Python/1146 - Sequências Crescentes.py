while True:
    X = int(input())
    if X == 0:
        break
    for c in range(1, X):
        print(f'{c} ', end='')
    print(X)
