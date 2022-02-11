n1, n2, n3, n4 = map(float, input().split())
media = ((n1*2) + (n2*3) + (n3*4) + n4)/10
if media >= 7:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
elif 5.0 <= media <= 6.9:
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    exam = float(input())
    media2 = (exam + media) / 2
    if media2 >= 5.0:
        print(f'Nota do exame: {exam:.1f}')
        print('Aluno aprovado.')
        print(f'Media final: {media2:.1f}')
    else:
        print(f'Nota do exame: {exam:.1f}')
        print('Aluno reprovado.')
        print(f'Media final: {media2:.1f}')
else:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')

