## Funções
# São rotinas de códigos que podem ser executadas quando tem seu nome invocado dentro do programa.
# Nós já estamos trabalhando com funções desde as aulas anteriores: Print, input, int, range etc (são instruções tb, mas a palavra formal é função).
# Essas funções acima são funções prontas que já vem instalado.

# As funções:
# Deixam nossos programas mais simples de compreender
# Confinam bugs para dentro delas
# Tornam programas mais portáveis
# Auxiliam no trabalho colaborativo

# Estrutura da função:
# exemplo de função: def realce():
# def (definition) = palavra-chave da função
# depois vem o nome da função
# () parênteses obrigatório
# :

def realce():
  #corpo da função
  print('|', '_' * 10, '|')
  print('|', '_' * 10, '|')
  # essa parte acima sozinha não vai fazer nada, pq precisa de um programa que invoque a função

# programa principal
realce() # aqui está invocando
print('     MENU')
realce()