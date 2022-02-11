a, b, c = map(float, input().split())
if a < b + c and b < a + c and c < b + a:
    p = a + b + c
    print(f'Perimetro = {p:.1f}')
else:
    area = ((a + b) * c) / 2
    print(f'Area = {area:.1f}')
