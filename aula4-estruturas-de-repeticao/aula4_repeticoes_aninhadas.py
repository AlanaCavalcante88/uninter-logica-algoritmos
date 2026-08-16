## Estruturas de repetições aninhadas
# é igual como faz no if else, pode colocar while dentro de while, pode colocar for dentro de for
# Não existe um limite de quantos aninhamentos pode colocar
# Pode misturar for com while, while com for

## escreva um algoritmo em Python que calcule a tabuada de todos os números de 1 até 10, e, para
# cada número, vamos calcular a tabuada multiplicando-o pelo intervalo de 1 até 10.

# Solução com 2x while
tabuada = 1
while (tabuada <= 10): # tabuada que começa do 1 e vai até o 10
  print(f'TABUADA DO {tabuada}: ')
  i = 1 # essa nova variável i começa do 1 e 
  while (i <= 10): # vai até o 10
    print(f'{tabuada} x {i} = {tabuada * i}') #
    i += 1 # aqui incrementa. Aqui nesse segundo while está calculando as tabuadas
  tabuada += 1

print('/----------------------------------/')


# Solução com 2x for
for tabuada in range(1, 11, 1):
  print(f'TABUADA DO {tabuada}: ')
  for i in range(1, 11, 1):
    print(f'{tabuada} x {i} = {tabuada * i}')

print('/----------------------------------/')

# Solução while + for
tabuada = 1
while (tabuada <= 10):
  print(f'TABUADA DO {tabuada}:')
  for i in range(1, 11, 1):
    print(f'{tabuada} x {i} = {tabuada * i}')
  tabuada += 1

print('/----------------------------------/')