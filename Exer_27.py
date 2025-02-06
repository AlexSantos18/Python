nome = str(input('Qual o seu nome completo '))
nome = nome.upper()
nome = nome.split()
n = int(len(nome)) - 1
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[n]))
