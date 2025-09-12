linhas = 3
colunas = 3
matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        itens = int(input(f'Digite um valor para [{i}, {j}]: '))
        linha.append(itens)
    matriz.append(linha)
print('-=' * 20)
for linha in matriz:
    for item in linha:
        print(f'[{item:^5}]', end='')
    print()