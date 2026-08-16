# Desenvolva um algoritmo que solicite ao usuário dos números inteiros. Imprima a soma desses dois números na tela

x = int(input('Informe um número inteiro: '))
y = int(input('Informe outro número inteiro: '))
res = x + y
# Maneira moderna
res = 'O resultado da soma de {} com {} é {}.'.format(x, y, x + y)
print(res)
# Maneira com f-string
res = f'O resultado da soma de {x} com {y} é {x + y}.'
print(res)