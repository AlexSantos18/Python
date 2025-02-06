vr = float(input('Qual o valor do Imovel: '))
salario = float(input('Qual o valor do salario bruto: '))
anos = int(input('Quantos anos para quitaçao: '))
prest = vr / (anos*12)
if prest >= (salario * 30)/100:
    print('\33[7;31mDesculpe mais seu financiamento não foi aprovado\033[m')
    print('Para pagar um Imovel R$ {:.2f} em {} anos, \nsua prestação \033[7;31mR$ {:.2f}\033[m deve ser '
          'acima de 30 por cento do seu salario'.format(vr,anos,prest))
else:
    print('Parabens o seu financiamento foi aprovado, sua prestaçao ficou R$ \033[7;32m{:.2f}\033[m'.format(prest))