# Variáveis
# Simples: armazenam somente um dado
# Compostas (strings): armazenam um conjunto de dados

# Estruturas de dados
# É um conjunto de dados organizados de uma maneira específica na memória do programa
# A maneira como os dados estão organizados na memória, como podem ser buscados, manipulados
# e acessados, é o que define e diferencia as estruturas de dados.

# Tupla
# Estrutura de dados estática
# A tupla é imutável
# Representada em Python por parênteses ( )

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila) #Vai acessar tudo o que está dentro da mochila e isso é tupla

#Agora se quiser acessar individualmente cada item da mochila, veja abaixo:
print(mochila[0]) # print do elemento 1 (índice 0) = Machado
print(mochila[1]) # print do elemento 2 (índice 1) = Camisa
print(mochila[0:2]) # print dos elementos 1 e 2 (índices 0 e 1) = Machado e Camisa
print(mochila[2:]) # print dos elementos a partir do índice 2
print(mochila[-1]) # print do último

# mochila[2] = 'Ovos' # Se fizer isso vai dá erro, pq a tupla é imutável, ela não suporta atribuição

for item in mochila:
  print(f'Na minha mochila tem: {item}\n')

# Desempacotamento de parâmetros em funções

# Suponha que você quer realizar o somatório de diversos valores, porém não sabe quantos valores serão somados. 
# Pode ser que seja somente 2, ou então 10, ou mesmo 100 números.
# Como criar uma função capaz de receber um número tão variável de parâmetros?

def soma(*num): # esse * significa no Python que será uma tupla de tamanho indefinido
  acumulador = 0
  print(f'Tupla: {num}\n')
  for i in num:
    acumulador += i
  return acumulador

# programa principal
print(f'Resultado: {soma(1,2)}\n')
print(f'Resultado: {soma(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)}\n')