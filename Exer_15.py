d = int(input('Digite a quantidade de dias: '))
k = int(input('Digite a quantidade de km rodados: '))
vr = float(d * 60.00) + (k *0.15)
print('O valor a pagar pelo aluguel é R$ {}'.format(vr))