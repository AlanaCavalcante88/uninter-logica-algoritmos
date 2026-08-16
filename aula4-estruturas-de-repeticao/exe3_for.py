# Escreva um algoritmo que calcule a médica dos números pares de 1 até 100 (1 e 100 inclusos).
# Implemente o laço usando for.

soma = 0 # variável acumuladora para soma
qtd = 0  # variável contadora para ir contando quantos números pares eu tenho

for i in range(1, 101, 1):
  if (i % 2 == 0): # aqui verifica se o número é par
    soma += i # se for par vai somando e contando
    qtd += 1 # contando
media = soma / qtd
print(f'A média dos pares de 1 até 100 é: {media}')