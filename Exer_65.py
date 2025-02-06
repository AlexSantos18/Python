import os
os.system('cls')
cont = 0
soma = 0
lista =[]
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    n2 = n
    resp = input('Quer continuar S/N: ')
    resp = resp.upper()
    cont += 1
    soma += n
    if resp == 'N':
        break
lista.sort()
print('Você digitou {} numeros a média foi {}'.format(cont, soma /cont))
print('O maior numero digitado foi {} e menor numero digitado foi {} '.format(lista[-1], lista[0]))

