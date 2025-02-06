print('###'*12)
print('        CADASTRE UMA PESSOA')
print('###'*12)
idade = []
sexo = []
verif = ''
contador_idade = 0
contador_masculino = 0
contador_feminino = 0
ano = 0
while True:
    ano = int(input('Idade : '))
    verif = input('Sexo: (M/F): ').upper() 
    if verif == 'M' or verif == 'F':
        resp = input('Quer continuar S/N: ').upper()
        if resp == 'S' or resp == 'N':
            if resp == 'S':
                sexo.append(verif)
                idade.append(ano)
            else:
                sexo.append(verif)
                idade.append(ano)
                idade.sort()
                sexo.sort()
                for itens in idade:
                    if itens <= 18:
                        contador_idade += 1
                for itens in sexo:
                    if itens == 'M':
                        contador_masculino += 1
                    else:
                        contador_feminino += 1
 
                print(f'Quantidade de Pessoas menor de idade {contador_idade}')
                print(f'Quantidade de Pessoas Masculino {contador_masculino}')
                print(f'Quantidade de Pessoas Feminino {contador_feminino}')
                break
        else:
            print('Digite (S) para continuar ou (N) para cancelar')
    else:
         print('Digite (F) para feminino ou (M) para masculino')
