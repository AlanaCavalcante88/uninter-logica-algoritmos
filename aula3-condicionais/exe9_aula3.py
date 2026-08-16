# Escreva um algoritmo que leia dois valores numéricos e que pergunte
# ao usuário qual operação ele deseja realizar.
# Adicão (+), subtração (-), multiplicação (*) ou divisão (/).
# Exiba na tela o resultado da operação desejada.

print('#####CALCULADORA#####')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione qualquer outra tecla para sair.')

op = input('Qual operação deseja realizar? ')
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

if (op == '+'):
  res = x + y
  print(f'Resultado: {x} + {y} = {res}')
elif (op == '-'):
  res = x - y
  print(f'Resultado: {x} - {y} = {res}')
elif (op == '*'):
  res = x * y
  print(f'Resultado: {x} * {y} = {res}')
elif (op == '/'):
  res = x / y
  print(f'Resultado: {x} / {y} = {res}')
else:
  print('Encerrando o programa...')