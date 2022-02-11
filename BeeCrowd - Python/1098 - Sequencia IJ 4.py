I = 0
J = 1
x = y = 0
while True:
    while y <= 3:
        while x in range(3):
            if I == 0 or I == 1 or I > 1.8:
                print(f'I={I:.0f} J={J:.0f}')
            elif J == 3:
                print(f'I={I:.0f} J={J:.0f}')
            else:
                print(f'I={I:.1f} J={J:.1f}')
            J += 1
            x += 1
        I += 0.2
        J -= 3
        J += 0.2
        y += 1
        x = 0
        if I > 2:
            break
    y = 0
    if I > 2:
        break