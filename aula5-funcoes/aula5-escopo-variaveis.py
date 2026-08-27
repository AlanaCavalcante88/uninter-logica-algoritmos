## Escopo de variáveis
# Um escopo é a propriedade que determina onde uma variável pode
# ser utilizada dentro de um programa.

# Escopo local
# Criado sempre que uma função é chamada.
# Variáveis criadas, seja no campo de um parâmetro ou dentro do corpo da função,
# fazem parte do escopo local daquela função e são chamadas de variáveis local.
# Essas variáveis só existem dentro daquela própria função.

# Escopo global
# Criado no programa principal.
# Variáveis globais pertencem a um escopo global e são variáveis criadas dentro do programa
# principal. Uma variável global existe também em todas as funções invocadas ao longo do programa.

# Ex1:
# def omelete():
#   ovos = 12 #variável local

# # programa principal
# omelete()
# print(ovos) # escopo global

# Ex2:
# def omelete():
#   print(ovos) #variável local

# # programa principal
# ovos = 12 # escopo global
# omelete()

# Ex3:
# def omelete():
#   ovos = 12 # aqui é uma variável
#   bacon()
#   print(ovos)

# def bacon():
#   ovos = 6 # e aqui é outra variável e como ela é local, por isso não substitui o 12. Essa variável com 6 é isolada, não enxerga e nem altera a de cima.

# # programa principal
# omelete()

# Ex4:
# def omelete():
#   ovos = 12 # aqui é uma variável local de omelete
#   print('Ovos da funcao omelete = ', ovos)

# def bacon():
#   ovos = 6 # variável local de bacon
#   print('Ovos do bacon = ', ovos)
#   omelete()
#   print('Ovos do bacon = ', ovos)

# # programa principal
# ovos = 2 # variável global
# bacon()
# print('Ovos  da variavel global ', ovos)

# Instrução global
def omelete():
  global ovos #A instrução global ovos avisa ao Python: "qualquer alteração nesta variável deve ser feita diretamente na variável global ovos"
  ovos = 6 # A linha ovos = 6 sobrescreve o valor 12 anterior no escopo global para 6.

# Programa principal
ovos = 12
omelete()
print(ovos)