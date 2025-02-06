n = 0
contador = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar] : '))
    if n == 999:
        break
    contador += 1
    soma = soma + n
print('Você digitou {} vezes e a soma dos valores digitados foram {}' .format(contador, soma))
print('fim')