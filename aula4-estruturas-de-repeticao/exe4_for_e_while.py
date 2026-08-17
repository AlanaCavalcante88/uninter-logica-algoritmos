# Realize a sequência de print com for e while:
#   a) Inteiros de 3 até 12, com 12 inclusos
#   b) Inteiros de 0 até 9, excluindo 9, com passo de 2

# a)
i = 3
while (i < 13):
  print(i)
  i += 1
print('terminada a opção a com while--------------------------------------')

# a)
i = 3
for i in range(i, 13, 1):
  print(i)
print('terminada a opção a com for--------------------------------------')

# b)
i = 0
while(i < 9):
  print(i)
  i += 2
print('terminada a opção b com while--------------------------------------')

# b)
for i in range(0, 9, 2):
  print(i)
print('terminada a opção b com for--------------------------------------')