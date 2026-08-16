# Valores Truthy e Falsey
# Dados não booleanos também podem ser trataodos como True ou False em uma condição, 
# seja esta de uma estrutura condicional ou de um laço

# Falsey / False
# O Python entende número zero (int ou float) e string vazia como false.

# Truthy / True
# Tudo que não for zero ou string vazia, o Python pode tratar como verdadeiro.

nome = '' # string vazia é falsey
while not nome: # Aqui está transformando nome em Truthy
  # encerra o laço quando nome não estiver vazio
  nome = input('Digite seu nome: ')

  valor = int(input('Digite um número qualquer: '))
  if valor: # Equivalente if valor != 0:
    print('Você digitou um valor diferente de zero.')
  else:
    print('Você digitou zero.')