n = int(input('Digite um numero para verificar se ele é primo: '))
c1 = 0
for c in range(1, n+1, 1):
    if n % c == 0:
        print(c, end=' ')
        c1 += 1
if c1 == 2:
    print('É um numero primo pois só é divisivel por 1 e por ele mesmo {}'.format(n))
else:
    print('O numero {} é dividivel por esses numeros portanto não é primo'.format(n) )