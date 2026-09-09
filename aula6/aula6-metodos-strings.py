# Uma string é imutável
# Mas, com listas, podemos alterá-la

s1 = list('Algoritmos')
print(s1) #print separado
print(''.join(s1)) #print agrupado

s1 [0] = 'a' #aqui está alterando o caractere de A -> a, e só é possível pq antes inseriu numa lista.
print(''.join(s1))

# Relação de métodos para uso com strings
# startswith - Verifica se caracteres existem no início da string
# endswith - Verifica se caracteres existem no final da string
# lower - Converte string para minúscula
# upper - Converte string para maiúscula
# find - Busca a primeira ocorrência de um padrão de caracteres em uma string
# rfind - Idêntico ao find, mas inicia a busca da direita para a esquerda
# center - Centraliza uma string
# ljust, rjust - Ajustam uma string com alinhamentos à esquerda ou à direita, respectivamente
# split - Divide uma string
# replace - Substitui caracteres em uma string
# lstrip, rstrip - Removem espaços em branco à esquerda ou à direita, respectivamente
# strip - Remove espaços em branco das extremidades

# Exemplos:
s1 = 'Lógica de Programação e Algoritmos'
s1.startswith('Lógica')

s1 = 'Lógica de Programação e Algoritmos'
s1.endswith('Algoritmos')

s1 = 'Lógica de Programação e Algoritmos'
s1.endswith('algoritmos') # aqui vai dá falso pq Algoritmo é diferente de algoritmo, o que pode ser feito está no exemplo abaixo

s1 = 'Lógica de Programação e Algoritmos'
s1.lower().endswith('algoritmos') # aqui primeiro converteu tudo para minúsculo e agora sim o resultado é verdadeiro.

s1 = 'Lógica de Programação e Algoritmos'
s1.lower().endswith('algoritmos')

s1 = 'Lógica de Programação e Algoritmos'
print(s1.upper())
print(s1.lower())

# Contando caracteres

s1 = 'Lógica de Programação e Algoritmos' 
s1.count('a') #Aqui o resultado será 3 pq ele não está contando o A maiúsculo, o que pode ser feito está no exemplo abaixo

s1 = 'Lógica de Programação e Algoritmos'
s1.lower().count('a') # aqui converteu tudo para a minúsculo e aí sim a contagem estará correta.

s1 = 'Um mafagafinho, dois mafagafinhos, três mafagafinhos...'
s1.lower().count('mafagafinho') # aqui está contando quantas vezes mafagafinho aparece.

# Quebrando strings

s1 = 'Um mafagafinho, dois mafagafinhos, três mafagafinhos...'
s1.split('') # quebrar uma string e jogar cada parte que quer em uma lista

# Substituindo strings

s1 = 'Um mafagafinho, dois mafagafinhos, três mafagafinhos...'
s1.replace('mafagafinho', 'gatinho') #substituir mafagafinho por gatinho e então substituirá todas as vezes que tiver mafagafinho na frase

s1 = 'Um mafagafinho, dois mafagafinhos, três mafagafinhos...'
s1.replace('mafagafinho', 'gatinho', 1) #substituir mafagafinho por gatinho e está informando que só quer substituir 1x

# Relação de métodos para validação de dados em strings (são importantes para verificações em cadastros etc)
# isalnum - Somente letras e números; acentos são aceitos
# isalpha - Somente letras; acentos são aceitos
# isdigit - Somente números
# isnumeric - Somente números; aceita também caracteres matemáticos, como frações
# isupper - Somente caracteres maiúsculos
# islower - Somente caracateres minúsculos
# isspace - Somente espaços; inclui TAB, quebra de linha, retorno etc
# isprintable - Somente caracteres possíveis de serem impressos na tela

s1 = 'Lógica de Programação e Algoritmos'
s2 = '42'
print(s1.isalnum()) # aqui vai dá false pq tem espaços
print(s1.isalnum())