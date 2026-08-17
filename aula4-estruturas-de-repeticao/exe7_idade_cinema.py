# Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes o preço do ingresso do cinema.
# Encerre o laço, usando um break quando o usuário digitar zero.
# Após encerrar o laço, apresente na tela o total de pessoas que compraram ingressos, o total de dinheiro arrecadado e a média de idade das pessoas.
# O cinema cobra preços diferentes para os ingressos, de acordo com a idade da pessoa. Se a pessoa tiver menor de 3 anos de idade, o ingresso será gratuito;
# Se tiver entre 3 e 12 anos, o ingresso custará R$ 15,00;
# Se tiver mais de 12 anos, custará R$ 30,00.

total = 0
dinheiro = 0
accIdades = 0

while True:
  idade = int(input('Qual a sua idade? '))  
  if (idade == 0):
    break

  total += 1
  accIdades += idade

  if (idade < 3):
    ingresso = 0
  else:
    if (idade > 12):
      ingresso = 30
    else:
      ingresso = 15

  dinheiro += ingresso

if (total > 0):
  media = accIdades / total
  print(f'\nTotal de pessoas: {total}\n')
  print(f'\nTotal arrecadado: {dinheiro}\n')
  print(f'\nMédia idades: {media}\n')

