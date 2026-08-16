print('Hello, world!')

nota = 8.5
disciplina = 'Lógica de Programação e Algoritmos'

print(nota)
print(disciplina)


#### Variáveis
# Não pode iniciar com:
# número: 2nota
# _ underscore: _nota
# !nota
# assentos e ç: preço


#### PEP 8 - Python Enhancement Proposals
# Conjunto oficial de regras e boas práticas do Python: https://peps.python.org/


#### Tipos primitivos de dados
# Numérico (inteiro e ponto flutuante) - int / float
# booleanos - true or false - armazena 1 (que é true) ou 0 (que é false)
# operadores booleanos - aqui é diferente de = (que aqui é atribuição)
# == igualdade
# > maior que
# < menor que
# >= maior ou igual a 
# <= menor ou igual a 
# != diferente

a = 1
b = 5

resposta = a == b
print(resposta)

resposta = a != b
print(resposta)

#### strings (cadeia de caracteres)
# São os textos
# Um número pode ser uma string, dependendo do contexto

frase = 'Olá, mundo!'
print(frase)

print(frase[0]) #Aqui vai mostrar o índice 0 da frase

#### Concatenação
# Juntar / somar duas strings

s1 = 'Lógica de Programação'
s1 = s1 + ' e Algoritmos'
print(s1)

s1 = 'A' + '-' * 10 + 'B'
print(s1)

s1 = 'A' + ' ' * 10 + 'B'
print(s1)


#### Composição com marcadores de posição
# Juntar diferentes variáveis e strings
# %d ou %i = Números inteiros
# %f = Números de ponto flutuante
# %s = Strings

nota = 8.9
s1 = 'Você tirou %f na disciplina de Algoritmos' % nota
print(s1) 

nota = 8.5
s1 = 'Você tirou %.2f na disciplina de Algoritmos' % nota
print(s1) 

nota = 8.5
disciplina = 'Lógica de Programação e Algoritmos'
s1 = 'Você tirou %.2f na disciplina de %s' % (nota, disciplina)
print(s1) 

# Composição moderna { }
nota = 8.5
disciplina = 'Lógica de Programação e Algoritmos'
s1 = 'Você tirou {} na disciplina de {}'.format(nota, disciplina)
print(s1) 

# Composição com f-string (esta é a maneira mais atual e fácil de composição)
nota = 8.5
disciplina = 'Lógica de Programação e Algoritmos'
s1 = f'Você tirou {nota} na disciplina de {disciplina}'
print(s1) 

# Fatiamento

s1 = 'Lógica de Programação e Algoritmos'
print(s1[0:6]) # aqui ele vai pegar do índice 0 ao 6

s1 = 'Lógica de Programação e Algoritmos'
print(s1[24:34]) # aqui ele vai pegar do índice 24 ao 34, pegando só a palavra algoritmos

s1 = 'Lógica de Programação e Algoritmos'
print(s1[:6]) # pega tudo desde o ínicio até o índice 6

s1 = 'Lógica de Programação e Algoritmos'
print(s1[24:]) # pega tudo começando no índice 24 até o final


#### Tamanho (length)
# Podemos descobrir o tamanho da cadeia de caracteres com uma função chamada len

s1 = 'Lógica de Programação e Algoritmos'
tamanho = len(s1)
print(tamanho)


#### Comando de entrada - input: comando, instrução, função 
idade = input('Qual a sua idade?')
print(idade)

nome = input('Qual o seu nome?')
print(f'Olá {nome}, seja bem-vindo!')


#### Convertendo dados de entrada (casting)
# O input do Python sempre retorna um dado do tipo string (sempre gera saída como string)
# Se quisermos um dado numérico, utilizamos a função int ou float antes do input
nota = float(input('Qual nota você recebeu na disciplina? '))
print(f'Você tirou nota {nota}.')


#### Fluxo de execução e teste de mesa
# Como se dá a execução

x = 1
y = 1
z = x + y # z = 2

x = x + 2 # Está alterando o valor de x, ou seja, x = 1 + 2 = 3
y = y - 1 # y = 1 - 1 = 0
z = x + y # z = 3 + 0 = 3

x = y + 1 # x = 0 + 1 = 1
y = x - 1 # y = 1 - 1 = 0
z = x + y # z = 1 + 0 = 1

print(z) # z = 1