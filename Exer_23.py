n = str(input('Digite um numero entre 0 e 9999: '))
print('Analisando o numero digitado ....')
num = int(n)
if num > 999:
    print('Unidade: {}\nDezena:  {}\nCentena: {}\nMilhar:  {}'.format(n[3], n[2], n[1], n[0]))
else:
    if num > 99:
        print('Unidade: {}\nDezena:  {}\nCentena: {}'.format(n[2], n[1], n[0]))
    else:
        if num > 9:
            print('Unidade: {}\nDezena:  {}'.format(n[1], n[0]))
        else:
            print('Unidade: {}'.format(n[0]))
