va1 = eval(input("Digite um valor: "))
va2 = eval(input("Digite um valor: "))
va3 = eval(input("Digite um valor: "))
va4 = eval(input("Digite um valor: "))
va5 = eval(input("Digite um valor: "))
numeros = (va1, va2, va3, va4, va5)
print(f"Os valores sao {numeros}")
print(f"O valor 9 apareceu {numeros.count(9)} vezes")
print(f"O valor 3 apareceu na posicao {numeros.index(3)+1} " if 3 in numeros else "O valor 3 nao foi digitado")
print("Os valores pares digitados foram: ", end="")
for n in numeros:
    if n % 2 == 0:
        print(n, end=" ")   