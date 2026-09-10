# Listas

# Estruturas de dados dinâmica 
# Podemos alterar dados e tamanho -> diferente de tuplas que são estáticas
# Indexadas por valores numéricos inteiros
# Representadas em Python por colchetes [ ]

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print('Tupla: ', mochila)

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print('Lista: ', mochila)

mochila[2] = 'Laranja'
print('Lista: ', mochila)

# Manipulando listas

mochila.append('Ovos') # Adiciona no final da lista
print('Lista com append:\n', mochila)

mochila.insert(1, 'Canivete') # Insere na posição informada
print('Lista com insert:\n', mochila)

del mochila[1] # Deleta do índice informado
print('Lista com del:\n', mochila)

mochila.remove('Ovos') # Deleta o dado informado
print('Lista com remove:\n', mochila)

# Cópia de listas

lista_original = [5, 7, 9, 11]
lista_referenciada = lista_original # quando faz isso aqui não está criando um novo espaço de memória e criando outra, só está apontando no endereço de memória para a outra lista
print(lista_original)
print(lista_referenciada)

lista_referenciada[0] = 2 # mesmo mexendo só na referenciada está alterando as duas
print(lista_original) # vai alterar as duas listas
print(lista_referenciada) # vai alterar as duas listas

# cópia (cada uma vai ter um bloco de memória para cada)

lista_original = [5, 7, 9, 11]
lista_referenciada = lista_original[:] # aqui está criando uma cópia na memória para a lista original
print(lista_original)
print(lista_referenciada)

lista_referenciada[0] = 2
print(lista_original) 
print(lista_referenciada) 

# O que são métodos?
# Uma lista é um objeto de uma classe dentro do Python
# Paradigmas de programação orientada a objetos (POO)
# Método é equivalente à função:
# mochila.append('Ovos')
# variável.função(parâmetro). Exemplo: a mochila é o nome do método, por isso ficou mochila.append
# append é um exemplo de método