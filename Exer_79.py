valores = list()
for c in range(1, 6):
    itens = int(input(f'Digite um valor na pisicao {c-1}: '))
    valores.append(itens) 
print(valores)
ordenado = sorted(valores)
menor = ordenado[0]
maior = ordenado[4]


keymenor = valores.index(menor)
keymaior = valores.index(maior)

print(ordenado)

print(f'O maior valor digitado foi {maior} e esta na posicao  {keymaior}')
print(f'O menor valor digitado foi {menor} e esta na posicao  {keymenor}')

