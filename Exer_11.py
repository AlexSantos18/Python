lar = int(input('Qual a largura dessa parede: '))
alt = int(input('Qual a altura dessa parede: '))
quad = int(alt * lar)
print('A area total desta parede é {} metros quadrados \nVocê vai precisar de {} litros de tinta pra pintar essa '
      'parede ' .format(quad , round(quad/2)))