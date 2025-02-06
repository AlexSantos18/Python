import os
os.system('cls')
print('*' *23)
print('OS 10 TERMOS DE UMA PA')
print('*' *23)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
contador = 10
while contador != 0:
    print(termo, end=' => ')
    termo += razao
    contador -=1
print('Acabou')