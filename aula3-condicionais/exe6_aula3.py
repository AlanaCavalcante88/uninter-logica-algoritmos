# Traduza as afirmações a seguir para condicionais em Python
# a) Se idade é maior que 60, escreva: "Você tem direitos aos benefícios!"
# b) Se dano é maior que 10 e escudo é igual a 0, escreva: "Você está morto!"
# c) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em True, escreva: "Você escapou!"

# a)
idade = int(input('Qual a sua idade? '))

if (idade >= 60):
  print('Você tem direitos aos benefícios!')

#################################################
# b)
dano = 13
escudo = 0

if (dano > 10 and escudo == 0):
  print('Você está morto!')

#################################################
# c)

norte = True
sul = False
leste = False
oeste = False

if (norte == True or sul == True or leste == True or oeste == True):
  print('Você escapou!')
