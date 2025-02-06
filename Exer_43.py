peso = float(input('Qual o seu peso: '))
altura = float(input('Qual a sua altura: '))
imc = peso /(altura * altura)
if imc <= 18.5:
    print('O imc dessa pessoa é de {:.1f}.'.format(imc))
    print('Voce esta abaixo do normal (procure um medico)')
elif imc <= 24.9:
    print('O imc dessa pessoa é de {:.1f}.'.format(imc))
    print('Voce esta normal.')
elif imc <= 29.9:
    print('O imc dessa pessoa é de {:.1f}.'.format(imc))
    print('Voce esta com sobrepeso.')
elif imc <= 34.9:
    print('O imc dessa pessoa é de {:.1f}.'.format(imc))
    print('Voce esta com obesidade grau I.')
elif imc <= 39.9:
    print('O imc dessa pessoa é de {:.1f}.'.format(imc))
    print('Voce esta com obesidade grau II.')
else:
    print('O imc dessa pessao é de {:.2f}.'.format(imc))
    print('Voce esta com obesidade grau III. (Aqui é sinal vermelho)')
    