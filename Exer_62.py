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
    if contador == 0:
        res = str.upper(input('Gostaria de mostrar mais termos S/N: '))
        if res == 'S':
            c = int(input('Mais quantos termos você gostaria de mostrar: '))
            contador = c
print('Acabou')