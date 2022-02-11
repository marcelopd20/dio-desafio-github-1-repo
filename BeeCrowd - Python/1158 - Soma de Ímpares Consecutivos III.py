N = int(input())
for c in range(0, N):
    X, Y = map(int, input().split())
    S = b = 0

    while b < Y:
        if X % 2 != 0:
            S += X
            b += 1
        X += 1
    print(S)