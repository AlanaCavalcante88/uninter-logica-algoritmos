#### Estrutura condicional simples
# condição -> se resultar em verdadeiro executa -> instruções
# condição -> se resultar em falso -> pula as instruções

# if ( x > y ):
# if é a estrutua condicional; ( x > y) é a condição lógica

# Lê dois valores inteiros e compara ambos
x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um segundo valor inteiro: '))

if (x > y):
  print('O primeiro valor é maior que o segundo!')
if (x < y):
  print('O segundo valor é maior que o primeiro!')

########################################################

#### Estrutura condicional composta
# condição -> se resultar em verdadeiro executa -> um bloco de instruções
# condição -> se resultar em falso executa -> outro bloco de instruções

# if (condição):
#     #instruções A
# else:
#     #instruções B

# Lê dois valores inteiros e compara ambos
x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um segundo valor inteiro: '))

if (x > y):
  print('O primeiro valor é maior que o segundo!')
else: 
  print('O segundo valor é maior que o primeiro!')

########################################################

# par ou ímpar (com condicional composta)
x = int(input('Digite um valor inteiro: '))
if (x % 2 == 0):
  print('O número é par!')
else:
  print('O número é ímpar!')

########################################################

# par ou ímpar (com condicional simples - NÃO É O RECOMENDADO)
x = int(input('Digite um valor inteiro: '))
if (x % 2 == 0):
  print('O número é par!')
if (x % 2 == 1):
  print('O número é ímpar!')