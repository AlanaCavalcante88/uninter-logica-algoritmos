## Escreva um algoritmo que calcule a sua média de notas em determinada disciplia.
# Vamos assumir que a média final é dada pela média aritmética de cinco notas digitadas.

## Variável acumuladora não tem nos exemplos acima, ela acumula valores variáveis a cada ciclo (como em soma = soma + x).

soma = 0 # Aqui é uma variável acumuladora e ela está inicializada em 0 (começa em 0 / sem nada)
cont = 1 # Variável de contagens das notas
while (cont <= 5):
  x = float(input(f'Digite a {cont} nota: '))
  soma = soma + x
  cont = cont + 1
media = soma / 5
print(f'Média final: {media}')