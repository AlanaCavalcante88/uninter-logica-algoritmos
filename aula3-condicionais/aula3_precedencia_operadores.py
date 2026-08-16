#### Precedência dos operadores
# 1. Parênteses
# 2. Operadores aritméticos de potenciação ou raiz
# 3. Operadores aritméticos de multiplicação, divisão e módulo
# 4. Operadores aritméticos de adição e subtração
# 5. Operadores relacionais
# 6. Operadores lógicos not
# 7. Operadores lógicos and
# 8. Operadores lógicos or
# 9. Atribuições

x = 10
y = 1
res = not x > y 
print(res)

#########################################
x = 10
y = 1
z = 5.5
res = (x > y) and (z == y) 
print(res)

#########################################

x = 10
y = 1
z = 5.5
res = x > y or not z == y and y != y + z / x 
# res = True or not False and True
# res = True or True and True
print(res)

