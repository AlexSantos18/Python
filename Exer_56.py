nome = []
idade = []
Sexo = []
maioridadehome = 0
nomevelho = ''
totalmulher20 = 0
for c in range(0, 4):
    print('------PESSOA {}ª------ '.format(c+1))
    nome.append(str.upper(input('Nome: ')))
    idade.append(int(input('Idade: ')))
    Sexo.append(str.upper(input('Sexo [M/F]: ')))
    if c == 0 and Sexo[c] == 'M':
        maioridadehome = idade[c]
        nomevelho = nome[c]
    if Sexo[c] == 'M' and idade[c] > maioridadehome:
        maioridadehome = idade[c]
        nomevelho = nome[c]
    if Sexo[c] == 'F' and idade[c] < 20:
        totalmulher20 += 1
s_idade = sum(idade)/ len(idade)
print('A media de idade do grupo é de {} anos.'.format(s_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehome, nomevelho))
print('Ao todo são {} mulheres com 20 anos'.format(totalmulher20))
    