# Crie um algoritmo que receba um valor do tipo inteiro via teclado.
# No entanto, o programa só deve aceitar, obrigatoriamente, valores inteiros e positivos.
# Qualquer valor negativo, ou igual a zero, deve ser rejeitado pelo programa e um novo valor deve ser solicitado.

x = int(input('Digite um valor maior do que zero: ')) # Aqui vc lê o valor
while (x <= 0): # Aqui verifica se x é menor ou igual a zero
  x = int(input('Digite um valor maior do que zero: ')) # então enquanto digitar algo inválido (que aqui é verdadeiro) vai ficar preso
print(f'Você digitou {x}. Encerrando o programa...') # quando a condição for satisfeita, que aqui é falso, contradizendo a linha 6, aí encerra.

