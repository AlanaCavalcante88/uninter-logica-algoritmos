# Imagine uma situação na qual você deve realizar o cadastro de uma lista de compras em um sistema.
# Cada produto comprado deverá ser registrado com seu nome, quantidade e valor unitário.

item = [] # criando duas listas vazias
mercado = [] # criando duas listas vazias

for i in range(3): # cadastra 3 itens
  item.append(input('Digite o nome do item: ')) # está fazendo um append, então vai adicionando cada item naquela lista que a princípio estava vazia
  item.append(int(input('Digite a quantidade: ')))
  item.append(float(input('Digite o valor: ')))
  mercado.append(item[:]) # aqui ele está fazendo uma cópia dessa lista que foi criado e adicionando com append dentro da lista do mercado
  item.clear() # tem que dar um clear pq tem que limpar a lista de itens para conseguir cadastrar o próximo
print(mercado)

# Abaixo tem outra forma de resolver mais simples

mercado = []
for i in range(3):
  nome = (input('Digite o nome do item: '))
  qtd = (int(input('Digite a quantidade: ')))
  valor = (float(input('Digite o valor: ')))
  mercado.append([nome, qtd, valor])
print(mercado)