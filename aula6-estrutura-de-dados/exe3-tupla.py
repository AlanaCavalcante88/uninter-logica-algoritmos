# Escreva um algoritmo que crie uma tupla com 10 palavras. Encontre dentro dessa tupla as vogais de cada palavra. Faça um print na tela com o nome da palavra e suas respectivas vogais.

palavras = ('Mario', 'Luidg', 'Peach', 'Yoshi', 'Bowser')

for palavra in palavras:
  print(f'\nPalavra: {palavra.upper()}. Vogais: ')
  for letra in palavra:
    if letra.lower() in 'aeiou': # convertendo tudo para minúsculo primeiro e depois verificar se a letra está contida nas vogais 'a', 'e', 'i', 'o' e 'u'
      print(letra.upper(), end=' ') # print da letra em maiúsculo e cada print sem dar enter com espaço