while True:
    X = int(input())
    S = 0
    if X == 0: break
    for c in range(X, X + 10):
        if c % 2 == 0:
            S += c
    print(S)