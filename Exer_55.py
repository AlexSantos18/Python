peso = []
for c in range(1, 6):
    peso.append(float(input('Peso da {}ª pessoa: '.format(c))))
peso.sort()
print('O maior peso é {}'.format(peso[4]))
print('O menor peso é {}'.format(peso[0]))    
 