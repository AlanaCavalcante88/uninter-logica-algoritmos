# break
# A instrução break seve para encerrar um laço de repetição abruptamente, independentemente do estado da 
# variável de controle do laço.

# Escreva um algoritmo que fique recebendo frases ou palavras digitadas pelo usuário.
# Encerre o algoritmo quando a palavra "sair" for digitada.

print('Digite uma mensarem que irei repetir para você!')
print('Para encerrar escreva "sair".')

while True:
  texto = input('')
  print(texto)
  if texto == 'sair':
    break
  print('Encerrando o programa...')

# continue
# O comando continue serve para retornar o laço ao início a qualquer momento,
# independentemente do estado da variável de controle da condicional do laço.

# Escreva um algoritmo que realize um login em um sistema.
# O usuário deve informar seu nome e senha.

while True:
  nome = input('Qual o seu nome? ')
  if (nome != 'Lenhadorzinho'):
    continue # volta para o início do laço

  senha = input('Qual a sua senha?')
  if (senha == 'UnInteR'):
    break # encerra o laço e avança para baixo

  print('Acesso condedido.')