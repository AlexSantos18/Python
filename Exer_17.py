from math import hypot
cp = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o cateto adjacente: '))
print('a hipotenusa vai medir {:.2f}'.format(hypot(cp,ca)))