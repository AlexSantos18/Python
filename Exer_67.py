import os
os.system('cls')
n = 0
while True:
    print('----'*10)
    n = int(input(('Quer ver a tabuada de qual valor : ')))
    print('----'*10)
    if n < 0:
        break
    for cont in range(0,11):
        print(f'{n} X {cont} = {n * cont}')

print('Programa Tabuada encerrado. Volte sempre!')

