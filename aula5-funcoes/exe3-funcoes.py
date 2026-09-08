# Escreva uma função que calcule o fatorial de um número recebido
# como parâmetro e retorne o seu resultado.
# Faça uma validação dos dados por meio de uma outra função, permitindo
# que somente valores positivos sejam aceitos.
# Crie o help da sua função.

def fatorial(num):

  fat = 1
  if (num == 0):
    return fat
  # esta parte só executa caso num seja > 0
  for i in range(1, num + 1):
    fat += i
  return fat

x = int(input('Digite um valor para calcular a fatorial: '))
print(f'{x}! = {fatorial(x)}')