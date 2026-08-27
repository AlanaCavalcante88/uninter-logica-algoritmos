## Parâmetros opcionais
# Podemos dar maior flexibilidade para nossas funções permitindo que nem 
# sempre se use todos os parâmetros na chamada da função.

def soma3(x, y, z): # aqui é função sem parâmetros opcionais, então se quiser invocar vou ter que obrigatoriamente sempre dizer os 3 valores que quero somar 
  res = x + y + z
  print(res)

def soma3(x = 0, y = 0, z = 0): #valor padrão para a variável, então se quiser omitir um valor, não vai ter problema
  res = x + y + z
  print(res)

soma3(1, 2, 3)
soma3(1, 2,) #z foi omitido
soma3(1) #y e z foram omitidos
soma3() #x, y e z foram omitidos