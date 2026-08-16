# for (para)

# Assim como o while, essa estrutura repete um bloco de instruções enquano uma condição se mantiver verdadeira.
# No entanto, diferentemente do while o for é empregado em situações em que o número de vezes que o laço irá executar é finito e bem definido.

for i in range(6): # Aqui por padrão o índice é 0, que o i começa em 0, por isso vai imprimir de 0 a 5.
  print(i)

print('/----------------------------/')
# ----------------------------------------------------------------------------------------------------------------
# para alterar o valor inicial do i, tem que colocar outros parâmetros, que são: Valor inicial do iterador, valor final do iterador e passo do iterador.
for i in range(1, 6, 1):
  print(i)

print('/----------------------------/')

# ----------------------------------------------------------------------------------------------------------------
for i in range(10, 0, -2): # vai diminuindo de 2 em 2
  print(i)

print('/----------------------------/')
# ----------------------------------------------------------------------------------------------------------------

# Varredura de strings
# Serve para pegar caractere por caractere, passando por todos os elementos da string

frase = "Lógica de Programação e Algoritmos"
for i in range(0, len(frase), 1): #len é para ir em todo o tamanho da string. O 1 aqui é a quantidade de passos que ele está andando.
  print(frase[i], end='')

print('/----------------------------/')