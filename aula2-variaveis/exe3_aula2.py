# Escreva as expressões em Python para:
# a) Atribuir o valor inteiro 3 à variável a
# b) Atribuir o valor 4 à variável break
# c) Atribuir à variável c o valor da expressão a * a + b * b

###################################################
a = 3
b = 4
c = print(a * a + b * b)


###################################################
# Execute as seguintes atribuições:
# s1 = 'ant'
# s2 = 'bat'
# s3 = 'cod'


s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# Agora utilizando operadores + e *, crie as saídas a seguir:
# a) `ant bat cod`
# b) `ant ant ant ant ant ant ant ant ant ant`
# c) `ant bat bat cod cod cod`
# d) `ant bat ant bat ant bat ant bat ant bat ant bat ant bat`
# e) `batbatcod batbatcod batbatcod batbatcod batbatcod` 

# a)
res = s1 + ' ' + s2 + ' ' + s3 
print(res)

###################################################
# b)
res = 10 * (s1 + ' ')
print(res)

###################################################
# c)
res = (s1 + ' ') + 2 * (s2 + ' ') + 3 * (s3 + ' ')
print(res)

###################################################
# d)
res = 7 * (s1 + ' ' + s2 + ' ')
print(res)

###################################################
# e)
res = 5 * (s2 + s2 + s3 + ' ')
print(res)