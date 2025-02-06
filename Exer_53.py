frase = str.upper(input('Digite um nome: '))
nome = frase.strip()
nome = ''.join(nome.split())
n = len(nome)
lista = []
ind = -1
for c in range(0, n, 1):
    lista.append(nome[ind])
    ind -= 1
    #print(lista)

n2 = ''.join(lista)
#print(n2)
if nome == n2:
    print('A frase digitada \33[7;31m{}\33[m é igual ao inverso \33[7;31m{}\33[m'.format(nome, n2))
    print('Portando é uma palindromo')
else:
    print('Essa frase digitada não é uma palindromo, pois ela inverso é \33[7;31m{}\33[m'.format(n2))