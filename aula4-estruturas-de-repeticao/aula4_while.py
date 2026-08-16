## Estrutura de repetição -> É uma estrutura no programa em que todas as instruções contidas nela se repetem de maneura indefinida,
# até que uma condição seja satisfeita. 
# Sinônimos: estrutura iterativa, laço de repetição ou loop de repetição.

## while (enquanto)
# Repete um bloco de instruções ENQUANTO determinada condição se mantiver verdadeira. ENQUANTO FOR VERDADEIRO EXECUTA!
# Caso contrário, ocorro o desvio para a primeira linha de código após este bloco de repetição.

x = 1
while(x <= 5):
  print(x)
  x = x + 1 # aqui está incrementando. Se não tiver essa linha, vai entrar em um loop infinito.


## Variável de controle
# Define a condição de parada com que o laço é executado.
# Chamamos de iterador a variável de controle que realiza a contagem do número de vezes queo laço está sendo executado.

inicial = int(input('Qual valor deseja iniciar a contagem? '))
final = int(input('Qual valor deseja encerrar a contagem? '))

x = inicial 
while (x <= final):
  # verifica se o número é par
  if (x % 2 == 0):
    print(x)
  x = x + 1 # 'x' é a variável contadora, pq é incrementada em um valor fixo a cada iteração, controlando o fluxo e o número de repetições do laço while.


  ## Variável acumuladora não tem nos exemplos acima, ela acumula valores variáveis a cada ciclo (como em soma = soma + x).