n = str(input('Digite um nome: ')).strip()
n = n.upper()
print('A letra A apareceu {} vezes na frase.'.format(n.count("A")))
print('A primeira letra A apareceu na posição {}'.format(n.find("A")+1))
print('A ultima letra A apareceu na posição {}'.format(n.rfind('A')+1))