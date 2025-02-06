print('*' *23)
print('OS 10 TERMOS DE UMA PA')
print('*' *23)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
for c in range(0, 10, 1):
    print(termo, end=' => ') 
    termo += razao
print('Acabou')
