print('========== lOJAS SANTOS ==========')
vr = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à Vista dinheiro/cheque')
print('[ 2 ] à vista cartao')
print('[ 3 ] 2x no cartão ')
print('[ 4 ] 3x ou mais no cartao ')
op = int(input('Qual a opção? '))
if op == 4:
    parcelas = int(input('Em quantas parcelas? '))
    juros = (vr *20)/100
    vr_total = juros + vr
    print('Sua compra sera parcelada em {} de R$ {:.2f} com juros.'.format(parcelas,(vr_total/parcelas)))
    print('Sua compra de R$ {:.2f} vai custar no final R$ {:.2f}'.format(vr,vr_total))
elif op == 1:
    vr_final = (vr * 10)/100
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(vr,(vr-vr_final)))
elif op == 2:
    vr_final = (vr * 5)/100
    print('Sua compra de R$ {:.2f} vai custa R$ {:.2f} no final.'.format(vr,(vr-vr_final)))
elif op == 3:
    print('Sua compra será parcelada em 2 vezes sem juros no valor R$ {:.2f}.'.format(vr/2))

      