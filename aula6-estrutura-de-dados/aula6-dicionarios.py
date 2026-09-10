# Dicionarios

# Estrutura de dados dinâmica
# Podemos alterar dados e tamanho
# Indexados por chaves (palavras-chave) -> essa é a diferença das listas, porque lá indexava por tipos numéricos (índice 0, índice 1...) e aqui pode indexar por palavra-chave
# Representados em Python por chaves {}

mochila = ('Laptop', 'Smartphone', 'Power Bank', 'Carregadores e Cabos')
print('Tupla: ', mochila)

mochila = ['Laptop', 'Smartphone', 'Power Bank', 'Carregadores e Cabos']
print('Lista: ', mochila)

mochila = {'Laptop': 1, 'Smartphone': 2, 'Power Bank': 3, 'Carregadores e Cabos': 4}
print('Dicionário: ', mochila)

game = {'nome':'Super Mario',
        'desenvolvedora':'Nintendo',
        'ano':1990}
print(game)

print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])

# Métodos para dicionários
# values: obtém somente os dados
# keys: obtém somente as chaves
# items: obtém o par chave:dado

print(game.values()) # vai retornar somente os valores
print(game.keys())

# Listas com dicionários
# Uma lista contendo, em cada índice, um dicionário

games = []

game1 = {'nome':'Super Mario',
        'desenvolvedora':'Nintendo',
        'ano':1990}

game2 = {'nome':'Zelda Ocarina of Time',
        'desenvolvedora':'Nintendo 64',
        'ano':1998}

game3 = {'nome':'Pokemon Yallow',
        'desenvolvedora':'Game Boy',
        'ano':1999}

games = [game1, game2, game3] # aqui cria uma lista com todos os games dentro
print(games)

# Dicionários com listas

games = {'nome':[ 'Super Mario', 'Zelda Ocarina of Time', 'Pokemon Yallow' ], # a palavra chave é nome e o valor são as inserções
         'videogame':[ 'Nintendo', 'Nintendo 64', 'Game Boy' ],
         'ano': [1990, 1998, 1999]}
print(games)

