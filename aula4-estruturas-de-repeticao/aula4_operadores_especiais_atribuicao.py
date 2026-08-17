## Operadores especiais de atribuição

# += -> exemplo x += 1 -> equivalente x = x + 1
# -= -> exemplo x -= 1 -> equivalente x = x - 1
# *= -> exemplo x *= 1 -> equivalente x = x * 2
# /= -> exemplo x /= 1 -> equivalente x = x / 2
# **= -> exemplo x **= 1 -> equivalente x = x ** 2
# //= -> exemplo x //= 1 -> equivalente x = x // 4

soma = 0 # Aqui é uma variável acumuladora e ela está inicializada em 0 (começa em 0 / sem nada)
cont = 1 # Variável de contagens das notas
while (cont <= 5):
  x = int(input(f'Digite o {cont} numero: '))
  soma += x
  cont += 1
print(f'Somatório: {soma}')