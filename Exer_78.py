valores = list()
for c in range(1, 6):
    itens = int(input(f'Digite um valor na pisicao {c-1}: '))
    valores.append(itens) 
print(valores)
ordenado = sorted(valores)
menor = ordenado[0]
maior = ordenado[4]
keymaior = []
keymenor = []

for i, itens in enumerate(valores):
    if itens == maior:
        keymaior.append(i)

print(f'O maior valor digitado foi {maior} e esta na posicao  {keymaior}')

for i, itens in enumerate(valores):
    if itens == menor:
        keymenor.append(i)

print(f'O menor valor digitado foi {menor} e esta na posicao  {keymenor}')

