# Match-case
# Surgiu no Python 3.10
# Equivalente ao Switch case do C / C++

# Escreva um algoritmo em Python em que o usuário escolhe se ele quer comprar maçãs, laranjas ou bananas.
# Deverá ser apresentado na tela, um menu com a opção 1 para maçãs, 2 para laranjas e 3 para bananas.
# Após escolhida a fruta, deve-se digitar quantas unidade se quer comprar.
# O algoritmo deve calcular o preço total a pagar do produto escolhido
# e mostrá-lo na tela. Considere que uma maçã custa R$ 2,30, uma
# laranja R$ 3,60 e uma banana R$ 1,85.

print('Escolha o que deseja comprar: ')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha? '))
qtd = int(input('Quantas unidades? '))

match (produto): 
  case 1:
    pagar = qtd * 2.3
    print(f'Você comprou {qtd} maçãs. Total à pagar R$ {pagar}')

  case 2:
    pagar = qtd * 3.6
    print(f'Você comprou {qtd} laranjas. Total à pagar R$ {pagar}')

  case 3:
    pagar = qtd * 1.85
    print(f'Você comprou {qtd} bananas. Total à pagar R$ {pagar}')

  case _: # qualquer coisa que não for as frutas acima
      print('Produto inexistente!')