linhas = 3
colunas = 3
matriz = []
par = 0

for i in range(linhas):
    linha = []
    for j in range(colunas):
        itens = int(input(f'Digite um valor para [{i}, {j}]: '))
        if (itens % 2 == 0):
            par += itens
        linha.append(itens)
    matriz.append(linha)

print('-=' * 20)
for linha in matriz:
    for item in linha:
        print(f'[{item:^5}]', end='')
    print()

print(f'A soma dos valores pares é {par}.')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')    