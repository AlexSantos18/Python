import math
n = float(input('Digite um angulo:'))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))
print('O Angulo de {:.2f} \nO SENO {:.2f}  \nO COSSENO {:.2f} \nA TANGENTE {:.2f}'
      .format(n,s,c,t))