from time import sleep
r1 = int(input('Digite um comprimento: '))
r2 = int(input('Digite um comprimento: '))
r3 = int(input('Digite um comprimento: '))
print(('CALCULANDO....'))
sleep(3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Você formou um triangulo')
else:
    print("Nao foi possivel formar um triangulo")