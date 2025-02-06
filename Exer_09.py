tab = int(input('Digite um numero para ver a tabuada : '))
n = 1
while n < 11:
    print('sua tabuada é {} x {:2} = {:2}' .format(tab, n, (tab * n)))
    n = n + 1
else:
    print('Fim da tabuada')
