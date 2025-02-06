import os
os.system('cls')
print(10*'=-=-')
print('       Sequência de Fiabonacci')
print(10*'=-=-')
termo1 = 0
n = int(input('Quantos termos você quer apresentar? '))
print('###'* 30)
print(termo1, end=' => ' )
termo2 = 1
print(termo2, end=' => ' )
soma = termo1 + termo2
n = n -2
while n != 0:
    print(soma, end=' => ' )
    termo1 = termo2
    termo2 = soma
    soma = termo1 + termo2
    n -=1
print('FIM')
print('###'*30)