sal = float(input('Digite o valor do salario R$ '))
if sal <= 1250.00:
    print('o valor da correção é R$ {:.2f}'.format(sal *15/100))
    print('O salario reajustado R$ {:.2f}'.format(sal+(sal *15/100)))
else:
    print('O valor da correção é R$ {:.2f}'.format(sal *10/100))
    print('O salario reajustado R$ {:.2f}'.format(sal+(sal *10/100)))