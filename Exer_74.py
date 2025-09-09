import random

numeros = random.sample(range(1, 100), 5) 
print(f"Os numeros sorteados foram: {numeros}")
print(f"O maior numero e {max(numeros)}")
print(f"O menor numero e {min(numeros)}")