n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
if media >= 6:
    print('Tirando {:.2f} e {:.2f}, sua media é {:.2f}'.format(n1,n2,media))
    print('O aluno foi APROVADO.')
else:
    print('Tirando {:.2f} e {:.2f}, sua media é {:.2f}'.format(n1,n2,media))
    print('O aluno está de RECUPERAÇAO')