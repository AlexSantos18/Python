times = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Bahia', 'Botafogo', 'Mirassol', 'Sao Paulo', 'Bragantino', 'Fluminense', 'Internacional', 'Ceara', 'Corinthians', 'Gremio', 'Atletico', 'Vasco', 'Santos', 'Vitoria', 'Juventude', 'Fortaleza', 'Sport')

print("=+=+"*10)
print("")
print(f"Os times sao: {times}")
print("")
print("=+=+"*10)
print("")
print(f"Os primeiros 5 colocdos sáo {times[:5]}")
print("")
print("=+=+"*10)
print("")
print(f"Os ultimos 4 colocados sao {times[-4:] }")
print("")
ordenado = sorted(times)
print("=+=+"*10)
print("")
print(f"Os times em ordem alfabetica e  {ordenado}")
print("")
print("=+=+"*10)
print("")
prosicao = (times.index("Bragantino")) # foi trocado pois náo tem Chapecoense em 2025
print(f"A posicao do Bragantino e {prosicao}")
print("")
print("=+=+"*10)



