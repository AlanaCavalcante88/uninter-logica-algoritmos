## Parâmetros em Funções
# dentro dos () da função pode colocar nomes de variáveis que a função pode pegar esses dados
# Parâmetros são os dados recebifos pelas funções
# O ato de enviar um dado para uma função é chamado de passagem de parâmetro

# def realce(s1):
# def palavra-chave
# realce é o nome da função
# s1 é a variável, ou seja, o parâmetro

# Ex1:
def realce(s1): # s1 é um parâmetro da função — pense nele como uma variável temporária ou uma "gaveta vazia" que serve para receber o valor que você envia de fora.
  #corpo da função
  print('|', '_' * 10, '|')
  print('|', '_' * 10, '|')
  print(s1)
  print('|', '_' * 10, '|')
  print('|', '_' * 10, '|')
  # essa parte acima sozinha não vai fazer nada, pq precisa de um programa que invoque a função

# programa principal
realce('     MENU') # aqui está invocando e esse texto entra na gaveta s1. O Python executa o corpo da função substituindo print(s1) por print('    MENU')

##########################################################################
# Ex2:
def sub2(x, y):
  res = x - y
  print(res)

# Programa principal
sub2(5, 7) # veja que a ordem do que você passa como parâmetro importa