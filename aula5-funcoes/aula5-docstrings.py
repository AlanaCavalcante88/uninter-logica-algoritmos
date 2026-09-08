## Docstrings
# Strings inseridas dentro de nosso código Python que explicam o funcionamento dele
# A string é colocada na primeira linha da definiçâo de uma funçâo

def soma(x=0, y=0, z=0):
  '''
  Explicaçâo do funcionamento da funçâo:
  Retorna o somatório de até 3 valores numéricos quaisquer.

  x: valor numérico (opcional)
  y: valor numérico (opcional)
  z: valor numérico (opcional)
  '''

  return x + y + z

print(soma(3,2))
help(soma) # para entender a função criada