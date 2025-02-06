import datetime
dataatual = datetime.date.today().year
print(dataatual)
maior = 0
menor = 0
for c in range(1, 8, 1):
    data = int(input('Em que que ano a {}ª pessoa nasceu? '.format(c)))
    anos = dataatual - data
    if anos >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E tambem tivemos {} pessoas menores de idade'.format(menor))  