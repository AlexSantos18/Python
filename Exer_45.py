import time 
import random
while True:
    print('Suas opções: ')
    print('[ 0 ] PEDRA')
    print('[ 1 ] PAPEL')
    print('[ 2 ] TESOURA')
    print('[ 9 ] SAIR')
    pc = int(random.randint(0,2))
    n = int(input('Hora de jogar? '))
    if n == 9:
        print('Saindo...')
        break
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')
    print('-=-=-'*5)
    if n == 0:
        if pc == 1:
            print('\33[7;32mComputador jogou PAPEL')
            print('Jogador jogou PEDRA')
            print('COMPUTADOR VENCE\33[m')
            print('-=-=-'*5)
        elif pc == 2:
            print('\33[7;32mComputador jogou TESOURA')
            print('Jogador jogou PEDRA')
            print('JOGADOR VENCE\33[m')
            print('-=-=-'*5)            
        else:
            print('\33[7;32mComputador jogou PEDRA')
            print('Jogador jogou PEDRA')
            print('DEU EMPATE, VAMOS DE NOVO\33[m')
            print('-=-='*5)   
    elif n == 1:
        if pc == 0:
            print('\33[7;32mComputador jogou PEDRA')
            print('Jogador jogou PAPEL')
            print('JOGADOR VENCE\33[m')
            print('-=-=-'*5)   
        elif pc == 1:
            print('\33[7;32mComputador jogou PAPEL')
            print('Jogador jogou PAPEL')
            print('DEU EMPATE, VAMOS DE NOVO\33[m')
            print('-=-=-'*5)   
        else:
            print('\33[7;32mComputador jogou TESOURA')
            print('Jogador jogou PAPEL')
            print('COMPUTADOR VENCE\33[m')
            print('-=-=-'*5)   
    elif n == 2:
        if pc == 0:
            print('\33[7;32mComputador jogou PEDRA')
            print('Jogador jogou TESOURA')
            print('COMPUTADOR VENCE\33[m')
            print('-=-=-'*5)   
        elif pc == 1:
            print('\33[7;32mComputador jogou PAPEL')
            print('Jogador jogou TESOURA')
            print('JOGADOR VENCE\33[m')
            print('-=-=-'*5)   
        else:
            print('\33[7;32mComputador jogou TESOURA')
            print('Jogador jogou TESOURA')
            print('DEU EMPATE, VAMOS DE NOVO\33[m')
            print('-=-=-'*5)   
    else:
        print('Escolha errada será encerrado')
        break

