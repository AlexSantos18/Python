n = 0 
cont = 0
total = 0
while True:
    n = int(input('Digite um numero [para parar 999] :'))
    if n == 999:
        break
    total += n 
    cont += 1
print(f'A soma dos {cont} numeros é {total}!')
