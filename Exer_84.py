galera = list()
dado = list()
while True:
    dado.append(str(input("Nome: ")))
    dado.append(int(input("peso: ")))
    galera.append(dado[:])
    dado.clear()
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp in "N":
        break
print("-=" * 30)
print(f"Ao todo, temos {len(galera)} pessoas cadastradas.") 

maiores = 0
menores = 0
kymaior = []
kymenor = []
for i, p in enumerate(galera):
    if p[1] >= 100:
        print(f"{p[0]} pesa {p[1]} kg e está acima do peso.")
        maiores += 1
        kymaior.append(i+1)
    else:
        print(f"{p[0]} pesa {p[1]} kg e está dentro do peso.")
        menores += 1
        kymenor.append(i+1)
print(f"Temos {maiores} acima do peso e estão na posiçao {kymaior} e {menores} dentro do peso na posiçao {kymenor}.")    # maior de idade = 21 anos