import os
os.system('cls')
fat = int(input('Digite um numero para calcular o fatorial: '))
fatoral = fat
controle = fat -1
while controle != 0:
    fat = fat * controle
    controle -=1
print('O fatorial de {}! é {}'.format(fatoral,fat))
