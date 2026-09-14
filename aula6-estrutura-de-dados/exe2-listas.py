# Dada uma lista contendo as notas de alunos em uma disciplina, escreva uma exmpressão para:
# notas = [9,7,7,10,3,9,6,6,2]
# a) Encontrar quantos alunos tiraram nota 7
# b) Alterar a última nota para 4
# c) Encontrar a maior nota
# d) Ordenar a lista de notas
# e) A média das notas

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

# a)
qtd_notas7 = notas.count(7)
print(f"Alunos que tiraram 7: {qtd_notas7}") 

# b) 
notas[-1] = 4
print(notas)

# c)
print(max(notas))

# d)
notas.sort()
print(notas)

# e)
print(sum(notas) / len(notas)) # sum = soma todos os itens da lista
