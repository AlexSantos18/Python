import os
os.system('cls')
import random
contador = 0
print('>>>'*10)
print('VAMOS JOGAR PAR OU IMPAR')
print('>>>'*10)
while True:
    n_pc = random.randrange(0,11)
    n = int(input('Diga um numero: '))
    resp = input('Par ou Impar?  P/I : ')
    resp = resp.upper()
    while True:
        if (resp != 'P') and (resp != 'I'):
            resp = input('Par ou Impar?  P/I : ')
            resp = resp.upper()
        else:
            break
    soma = n + n_pc
    resto = soma % 2
    print(f'jogador jogou {n} e computador jogou {n_pc} a soma foi {soma}')
    if resto == 0:
        if resp == 'P':
            print('PAR')
            print('Jogador Ganhou!!!')
            contador +=1
            print(f'Jogador Ganhou {contador} vezes')
            print('>>>'*10)
        else:
            print('PAR')
            print('Computador Ganhou!!!')
            break
    else:
        if resp == 'I':
            print('IMPAR')
            print('Jogador Ganhou!!!')
            contador += 1
            print(f'Jogador Ganhou {contador} vezes')
            print('>>>'*10)
        else:
            print('IMPAR')
            print('Computador Ganhou!!!')
            break


