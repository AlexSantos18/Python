valores = list()

while True:
    itens = int(input("Digite uma valor: "))
    if itens in (valores):
        print("Valor ja consta da lista digite outro")
    else:
        valores.append(itens)
        resp = input("Deseja continuar S/N: ")
        if (resp == "s") or (resp == "S"):
            continue
        else:
            break
valores.sort()
print(f'Os valores ordenados foram {valores}')
