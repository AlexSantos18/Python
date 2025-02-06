while True:
    n = int(input('Digite um numero inteiro: '))
    print('Escolha uma das bases para conversão: ')
    print('_________'*4)
    print('|[ \33[32m1\33[m ] converter para BINARIO      |')
    print('|[ \33[32m2\33[m ] converter para OCTAL        |')
    print('|[ \33[32m3\33[m ] converter para HEXADECIMAL  |')
    print('|[ \33[32mx\33[m ] selecione X para sair       |')
    print('_________'*4)
    resposta = str(input('Digite a opçao que deseja converter: '))
    if resposta == 'x' or resposta == 'X':
        break
    elif resposta == '1':
        s = bin(n)
        s1 = s[2:]
        print('{} convertido em BINARIO'.format(s1))
    elif resposta == '2':
        print('{} convertido em OCTAL'.format(oct(n)))
    elif resposta == '3':
        print('{} convertido em HEXADECIMAL'.format(hex(n)))
    elif resposta != '1':
        print('\33[31mOpção errada o programa sera encerado!\33[m')
        break
