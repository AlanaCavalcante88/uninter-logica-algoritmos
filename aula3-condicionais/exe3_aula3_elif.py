#### elif (else if - senão se)
# Escreva um algoritmo que leia um nome e uma idade.
# Caso o nome digitado seja Alana, escreva isso na tela.
# Caso o usuário digite qualquer outro nome, verifique sua idade.
# Se for menor que 18 anos, informe que é menor de idade.
# Se for maior que 100, inform que esta pessoa possivelmente não existe.

nome = (input('Qual o seu nome? '))
idade = int(input('Qual a sua idade? '))

if nome == 'Alana':
  print('Olá, Alana!')
elif idade < 18:
  print('Você não é a Alana! E é menor de idade.')
elif idade > 100:
  print('Diferente de você, a Alana não é imortal!')
