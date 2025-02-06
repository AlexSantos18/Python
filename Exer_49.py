n = int(input('Digite um numero para ver a tabuada entre 1 e 10: '))
for c in range(0, 11, 1):
    print('{}  X  {:2}  =  {:2}'.format(n, c, n*c) )
print('FIM')