import datetime
data = datetime.date.today().year
nasc = int(input('Ano de nascimento: '))
dif = data - nasc
if dif <= 9:
    print('O atleta tem {} anos.'.format(dif))
    print('Classificação : MIRIM')
elif dif <= 14:
    print('O atleta tem {} anos.'.format(dif))
    print('Classificação : INFANTIL')
elif dif <= 19:
    print('O atleta tem {} anos.'.format(dif))
    print('Classificação : JUNIOR')
elif dif <= 25:
    print('O atleta tem {} anos.'.format(dif))
    print('Classificação : SENIOR')
else:
    print('O atleta tem {} anos.'.format(dif))
    print('Classificação : MASTER')

    
