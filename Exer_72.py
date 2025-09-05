estenso = ('Zero','Um' , 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    escolha = eval(input("Escolha um numero de 0 a 20: "))
    if (escolha < 0) or (escolha > 20):
         print('Escolha fora da faixa')
    else:
        print(f'O numero escolhido foi {estenso[escolha]}')
        break
            

