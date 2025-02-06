import datetime
data = datetime.date.today().year
ano = int(input('Ano de nascimento: '))
anos = data - ano
falta = 18 - anos 
if anos < 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano,anos,data))
    print('Ainda falta {} anos para o alistamento.'.format(falta))
    print('Seu alistamento será em {}'.format(data+falta))
elif anos > 18:
    print('Voce é maor de idade ja fez o alistamento')
    print('Voce fez o alistamento em {}'.format(data+falta))
else:
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano,anos,data))
    print('Seu alistamento será esse ano {}'.format(data+falta))

    