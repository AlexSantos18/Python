import os

def calculadora(n):
    for index in range(0, 11):
        print('{} X {} = {}'.format(n, index, n * index))
    return n

os.system('cls')
tab = int(input("Digite uma tabuada: "))
calculadora(tab)
