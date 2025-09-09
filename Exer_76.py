lista = ("Lapis", 0.99, "Borracha", 1.20, "Caderno", 18.80, "Estojo", 42.50, "Transferidor", 3.60, "Compasso", 15.99, "Mochila", 240.00, "Canetas", 12.40, "Livro", 56.90)
print("         Lista de Preços")
print("-" * 35)
total = len(lista)
for item in lista:
    if isinstance(item, str):
        print(f"{item:<25}", end="")
    else:
        print(f"R$ {item:>7.2f}")
print("-" * 35)
print(f"Total de itens: {total // 2:>19}")
print(f"Total da lista:          R$ {sum(lista[1::2]):>7.2f}")