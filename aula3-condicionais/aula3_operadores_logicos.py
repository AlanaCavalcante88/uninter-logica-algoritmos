#### Operadores lógicos em Python

# not = não = negação
# and = e = conjunção
# or = ou = disjunção

# not
# Serve para negar um resultado lógico ou o resultado de uma expressão booleana
# Na prática, isso significa que o resultado final de uma expressão será invertido
x = True
y = False
print(not x) # aqui vira False
print(not y) # aqui vira True

# and
# Este operador irá prover um resultado verdadeiro se, e somente se, ambas as 
# entradas forem verdadeiras
x = False
y = True
print(x and y)

# or
# Este operador irá prover um resultado verdadeiro se ao menos uma das 
# entradas for verdadeira
x = False
y = True
print(x or y)