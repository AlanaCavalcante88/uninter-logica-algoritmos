# rotina x procedimento
# Procedimento (procedure) - uma rotina sem retorno
# Função - uma rotina que retorna um dado a quem a invocou.

# Ex1:

def soma3(x = 0, y = 0, z = 0):
  res = x + y + z
  return res # aqui ele está retornando para o programa principal

# programa principal
retornado = soma3(1,2,3)
print(retornado)

# forma alternativa simplificada do programa principal acima
print(soma3(2,2))

# programa principal
retornado1 = soma3(1, 2, 3)
retornado2 = soma3(1,2)
retornado3 = soma3()
print(f'Somatórios: {retornado1}, {retornado2} e {retornado3}.')