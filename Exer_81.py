valores = list()
while True:
    itens = int(input("Digite um valor para a lista: "))
    valores.append(itens)
    resp = input("Deseja continuar a incluir S/N: ")
    if (resp == 's') or (resp == 'S'):
        continue
    else:
        break
quantidade = len(valores)
valores.sort(reverse=True)
print(f'A quantidade de elementos digitados foi {quantidade}')
print(f"Lista em ordem decrecente {valores}")
if 5 in (valores):
    print("O numero 5 foi encontrado na lista")
else:
    print("Nao foi encontrado o numero 5 na lista")
        