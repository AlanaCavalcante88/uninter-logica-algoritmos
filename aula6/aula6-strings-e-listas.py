# Strings e listas dentro de listas
# Dupla indexação é para acessar um caractere de uma string que está dentro da lista
# O primeiro índice é referente a cada item da lista
# O segundo índice é referente a cada caractere da string
# Assim, podemos acessar não só cada dado dentro da lista, mas também cada caractere das strings de um índice da lista.

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila[0]) # o resultado vai ser só Machado

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila[0][0]) # o resultado vai ser só M, pq Machado é índice 0 e dentro de machado o M é índice 0
print(mochila[2][1]) # o resultado vai ser a do Bacon, pq o Bacon é índice 2 e dentro dele a é índice 1

# Para iterar caractere por caractere
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
for item in mochila:
  for letra in item:
    print(letra, end='') #esse end serve para colocar um caractere do lado do outro sem dar quebra de linha
  print()

# Listas dentro de listas
# Ex: mochila = [['Cebola', 0.39], ['Tomate', 0.49], ['Maçã', 0.89]]
# Se quiser pegar cada índice inteiro, é só acessar por exemplo o índice 0, então vai pegar todo o colchete ['Cebola', 0.39]
# Mas se quiser pegar individualmente cada item que tiver dentro da lista, no caso acima, quero só o valor da cebola, então é o índice [0] e [1]