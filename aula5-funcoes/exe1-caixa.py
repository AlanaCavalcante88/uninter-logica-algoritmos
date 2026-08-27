# Escreva uma rotina que crie uma borda ao redor de uma palavra, para destacá-la como sendo um título.
# A rotina deve receber como parâmetro a palavra a ser destacada.
# O tamanho da caixa de texto deverá ser adaptável, de acordo com o tamanho da palavra.

def caixa(s1):
  tam = len(s1)

  # só imprime caso exista algum caractere

  if tam:
    print('+', '-' * tam, '+')
    print('|', s1, '|')
    print('+', '-' * tam, '+')

# programa principal
caixa('Olá, Mundo!')
caixa('Alana')
